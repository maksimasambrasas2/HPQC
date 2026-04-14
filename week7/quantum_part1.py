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
    """Apply a gate to the named qubits."""
    global workspace

    for name in names:
        tosQubit(name)

    workspace = np.reshape(workspace, (-1, gate.shape[0]))
    np.matmul(workspace, gate.T, out=workspace)


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


# Example / Demo Functions

def demo_push_and_gate():
    print("\n--- Demo 1: Push + Hadamard ---")
    reset_workspace()
    pushQubit("Q1", [1, 0])
    print("Initial workspace:", np.reshape(workspace, (1, -1)))
    applyGate(H_gate, "Q1")
    print("After H gate:", np.reshape(workspace, (1, -1)))
    print("Q1 probabilities:", probQubit("Q1"))


def demo_swap():
    print("\n--- Demo 2: Swap qubits ---")
    reset_workspace()
    pushQubit("Q1", [1, 0])
    pushQubit("Q2", [0.6, 0.8])
    print("Before moving Q1 to TOS:", np.reshape(workspace, (1, -1)))
    print("Name stack:", namestack)
    tosQubit("Q1")
    print("After moving Q1 to TOS:", np.reshape(workspace, (1, -1)))
    print("Name stack:", namestack)


def demo_measurement():
    print("\n--- Demo 3: Measurement ---")
    reset_workspace()
    pushQubit("Q1", [1, 0])
    applyGate(H_gate, "Q1")
    pushQubit("Q2", [0.6, 0.8])
    print("Q1 probabilities:", probQubit("Q1"))
    print("Q2 probabilities:", probQubit("Q2"))
    result_q1 = measureQubit("Q1")
    result_q2 = measureQubit("Q2")
    print("Measured Q1, Q2:", result_q1, result_q2)


def demo_toffoli_truth_table():
    print("\n--- Demo 4: Toffoli truth table sample ---")
    reset_workspace()
    outputs = []

    for _ in range(16):
        reset_workspace()
        pushQubit("Q1", [1, 1])
        pushQubit("Q2", [1, 1])
        pushQubit("Q3", [1, 0])
        applyGate(TOFF_gate, "Q1", "Q2", "Q3")
        q3 = measureQubit("Q3")
        q2 = measureQubit("Q2")
        q1 = measureQubit("Q1")
        outputs.append(q1 + q2 + q3)

    print(",".join(outputs))


def main():
    np.random.seed(42)  # make sample output reproducible
    demo_push_and_gate()
    demo_swap()
    demo_measurement()
    demo_toffoli_truth_table()


if __name__ == "__main__":
    main()
