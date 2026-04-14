import numpy as np

# Global workspace and name stack
workspace = np.array([[1.]], dtype=np.complex128)
namestack = []


# Basic Gates

X_gate = np.array([[0, 1],
                   [1, 0]], dtype=np.complex128)

Y_gate = np.array([[0, -1j],
                   [1j, 0]], dtype=np.complex128)

Z_gate = np.array([[1, 0],
                   [0, -1]], dtype=np.complex128)

H_gate = np.array([[1, 1],
                   [1, -1]], dtype=np.complex128) * np.sqrt(1 / 2)

S_gate = np.array([[1, 0],
                   [0, 1j]], dtype=np.complex128)

T_gate = np.array([[1, 0],
                   [0, np.exp(np.pi / -4j)]], dtype=np.complex128)

Tinv_gate = np.array([[1, 0],
                      [0, np.exp(np.pi / 4j)]], dtype=np.complex128)

CNOT_gate = np.array([[1, 0, 0, 0],
                      [0, 1, 0, 0],
                      [0, 0, 0, 1],
                      [0, 0, 1, 0]], dtype=np.complex128)

CZ_gate = np.array([[1, 0, 0, 0],
                    [0, 1, 0, 0],
                    [0, 0, 1, 0],
                    [0, 0, 0, -1]], dtype=np.complex128)

SWAP_gate = np.array([[1, 0, 0, 0],
                      [0, 0, 1, 0],
                      [0, 1, 0, 0],
                      [0, 0, 0, 1]], dtype=np.complex128)

TOFF_gate = np.array([[1, 0, 0, 0, 0, 0, 0, 0],
                      [0, 1, 0, 0, 0, 0, 0, 0],
                      [0, 0, 1, 0, 0, 0, 0, 0],
                      [0, 0, 0, 1, 0, 0, 0, 0],
                      [0, 0, 0, 0, 1, 0, 0, 0],
                      [0, 0, 0, 0, 0, 1, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 1],
                      [0, 0, 0, 0, 0, 0, 1, 0]], dtype=np.complex128)


# Core Stack-Machine Functions

def reset_workspace(complex_mode=True):
    """Reset the quantum workspace and name stack."""
    global workspace, namestack
    if complex_mode:
        workspace = np.array([[1.+0j]], dtype=np.complex128)
    else:
        workspace = np.array([[1.]], dtype=np.float64)
    namestack = []


def pushQubit(name, weights):
    """Push a qubit with a given name and weights onto the stack."""
    global workspace, namestack

    if workspace.shape == (1, 1):
        namestack = []

    namestack.append(name)

    weights = np.array(weights, dtype=workspace.dtype)
    weights = weights / np.linalg.norm(weights)

    workspace = np.reshape(workspace, (1, -1))
    workspace = np.kron(workspace, weights)


def tosQubit(name):
    """Move the named qubit to the top of the stack."""
    global workspace, namestack

    k = len(namestack) - namestack.index(name)

    if k > 1:
        namestack.append(namestack.pop(-k))
        workspace = np.reshape(workspace, (-1, 2, 2 ** (k - 1)))
        workspace = np.swapaxes(workspace, -2, -1)


def applyGate(gate, *names):
    """Apply a gate to the named qubits, supporting controlled behaviour."""
    global workspace

    if list(names) != namestack[-len(names):]:
        for name in names:
            tosQubit(name)

    workspace = np.reshape(workspace, (-1, 2 ** len(names)))
    subworkspace = workspace[:, -gate.shape[0]:]
    np.matmul(subworkspace, gate.T, out=subworkspace)


def probQubit(name):
    """Return probabilities for the named qubit being 0 or 1."""
    global workspace

    tosQubit(name)
    workspace = np.reshape(workspace, (-1, 2))
    prob = np.linalg.norm(workspace, axis=0) ** 2
    return prob / prob.sum()


def measureQubit(name):
    """Measure the named qubit, collapse the state, and pop it."""
    global workspace, namestack

    prob = probQubit(name)
    measurement = np.random.choice(2, p=prob)
    workspace = workspace[:, [measurement]] / np.sqrt(prob[measurement])
    namestack.pop()
    return str(measurement)


# Multi-controlled gate helper

def TOFFn_gate(ctl, result):
    """Generalised multi-control NOT using ancilla qubits."""
    n = len(ctl)

    if n == 0:
        applyGate(X_gate, result)
    elif n == 1:
        applyGate(CNOT_gate, ctl[0], result)
    elif n == 2:
        applyGate(TOFF_gate, ctl[0], ctl[1], result)
    elif n > 2:
        k = 0
        while "temp" + str(k) in [str(x) for x in namestack]:
            k += 1

        temp = "temp" + str(k)
        pushQubit(temp, [1, 0])
        applyGate(TOFF_gate, ctl[0], ctl[1], temp)
        new_ctl = ctl[2:] + [temp]
        TOFFn_gate(new_ctl, result)
        applyGate(TOFF_gate, ctl[0], ctl[1], temp)
        measureQubit(temp)


# Grover Part 2 Oracles

def zero_booleanOracle(qubits, result):
    """Return 1 in result if all qubits are zero, else 0."""
    for qubit in qubits:
        applyGate(X_gate, qubit)

    TOFFn_gate(qubits.copy(), result)

    for qubit in qubits:
        applyGate(X_gate, qubit)


def zero_phaseOracle(qubits):
    """Phase flip when all input qubits are zero."""
    for qubit in qubits:
        applyGate(X_gate, qubit)

    applyGate(Z_gate, *namestack)

    for qubit in qubits:
        applyGate(X_gate, qubit)


def sample_phaseOracle(qubits):
    """
    Sample phase oracle from the tutorial.
    Flips phase when all qubits except qubit 1 are one.
    """
    applyGate(X_gate, qubits[1])
    applyGate(Z_gate, *namestack)
    applyGate(X_gate, qubits[1])


# Grover Search

def groverSearch(n, printProb=True):
    """
    Perform Grover's search for n qubits.
    Uses the sample phase oracle from the tutorial.
    """
    optimalTurns = int(np.pi / 4 * np.sqrt(2 ** n) - 1 / 2)
    qubits = list(range(n))

    reset_workspace(complex_mode=True)

    for qubit in qubits:
        pushQubit(qubit, [1, 1])

    probability_history = []

    for _ in range(optimalTurns):
        sample_phaseOracle(qubits)

        for qubit in qubits:
            applyGate(H_gate, qubit)

        zero_phaseOracle(qubits)

        for qubit in qubits:
            applyGate(H_gate, qubit)

        probs = probQubit(qubits[0])
        probability_history.append(probs.copy())

        if printProb:
            print(probs)

    result_bits = []
    for qubit in reversed(qubits):
        result_bits.append(measureQubit(qubit))

    result = "".join(result_bits)
    print("Measured result:", result)
    return result, probability_history


# Demo runner

def main():
    np.random.seed(42)

    print("--- Grover's Search Demo (n = 6) ---")
    groverSearch(6, printProb=True)


if __name__ == "__main__":
    main()
