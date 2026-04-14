import time
import numpy as np
import torch as pt

pt.autograd.set_grad_enabled(False)

# Device setup

if pt.cuda.is_available():
    DEVICE = pt.device("cuda")
    print("GPU available")
else:
    DEVICE = pt.device("cpu")
    print("Sorry, only CPU available")

workspace = pt.tensor([[1.0]], device=DEVICE, dtype=pt.float32)
namestack = []


# Basic gates (NumPy definitions, converted when used)

X_gate = np.array([[0, 1],
                   [1, 0]], dtype=np.float32)

H_gate = np.array([[1, 1],
                   [1, -1]], dtype=np.float32) * np.sqrt(1 / 2)

Z_gate = H_gate @ X_gate @ H_gate


# Core simulator functions (PyTorch version)

def reset_workspace(device=DEVICE):
    global workspace, namestack
    workspace = pt.tensor([[1.0]], device=device, dtype=pt.float32)
    namestack = []


def pushQubit(name, weights):
    global workspace, namestack

    if (workspace.shape[0], workspace.shape[1]) == (1, 1):
        namestack = []

    namestack.append(name)

    weights = np.array(weights, dtype=np.float32)
    weights = weights / np.linalg.norm(weights)
    weights = pt.tensor(weights, device=workspace.device, dtype=workspace.dtype)

    workspace = pt.reshape(workspace, (1, -1))
    workspace = pt.kron(workspace, weights)


def tosQubit(name):
    global workspace, namestack

    k = len(namestack) - namestack.index(name)

    if k > 1:
        namestack.append(namestack.pop(-k))
        workspace = pt.reshape(workspace, (-1, 2, 2 ** (k - 1)))
        workspace = pt.swapaxes(workspace, -2, -1)


def applyGate(gate, *names):
    global workspace

    if list(names) != namestack[-len(names):]:
        for name in names:
            tosQubit(name)

    workspace = pt.reshape(workspace, (-1, 2 ** len(names)))
    subworkspace = workspace[:, -gate.shape[0]:]

    gate_t = pt.tensor(gate.T, device=workspace.device, dtype=workspace.dtype)

    if workspace.device.type == "cuda":
        pt.matmul(subworkspace, gate_t, out=subworkspace)
    else:
        subworkspace[:, :] = pt.matmul(subworkspace, gate_t)


def probQubit(name):
    global workspace

    tosQubit(name)
    workspace = pt.reshape(workspace, (-1, 2))
    prob = pt.linalg.norm(workspace, axis=0) ** 2
    prob = pt.Tensor.cpu(prob).numpy()
    return prob / prob.sum()


def measureQubit(name):
    global workspace, namestack

    prob = probQubit(name)
    measurement = np.random.choice(2, p=prob)
    workspace = workspace[:, [measurement]] / np.sqrt(prob[measurement])
    namestack.pop()
    return str(measurement)


# Grover oracles

def sample_phaseOracle(qubits):
    applyGate(X_gate, qubits[1])
    applyGate(Z_gate, *namestack)
    applyGate(X_gate, qubits[1])


def zero_phaseOracle(qubits):
    for q in qubits:
        applyGate(X_gate, q)
    applyGate(Z_gate, *namestack)
    for q in qubits:
        applyGate(X_gate, q)


# Grover search

def groverSearch(n, printProb=True):
    qubits = list(range(n))

    for q in qubits:
        pushQubit(q, [1, 1])

    turns = int(np.pi / 4 * np.sqrt(2 ** n) - 1 / 2)

    prob_history = []

    for _ in range(turns):
        sample_phaseOracle(qubits)

        for q in qubits:
            applyGate(H_gate, q)

        zero_phaseOracle(qubits)

        for q in qubits:
            applyGate(H_gate, q)

        if printProb:
            probs = probQubit(qubits[0])
            prob_history.append(probs.copy())
            print(probs)

    result = "".join(measureQubit(q) for q in reversed(qubits))
    print("Measured result:", result)
    return result, prob_history


# Main

def main():
    np.random.seed(42)

    print("\n--- Running Grover search with current device ---")
    reset_workspace(device=DEVICE)
    t0 = time.process_time()
    result, prob_history = groverSearch(8, printProb=True)
    elapsed = time.process_time() - t0
    print(f"Runtime on {DEVICE.type.upper()}: {elapsed:.6f} s")

    print("\n--- Optional CPU comparison ---")
    cpu_device = pt.device("cpu")
    reset_workspace(device=cpu_device)
    t1 = time.process_time()
    result_cpu, _ = groverSearch(8, printProb=False)
    elapsed_cpu = time.process_time() - t1
    print(f"Runtime on CPU: {elapsed_cpu:.6f} s")


if __name__ == "__main__":
    main()
