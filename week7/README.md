# Week 7: Program Your Own Quantum Computer – Part 1

## Files Included

- `quantum_part1.py` - Python implementation of the Part 1 quantum computer simulator tutorial

---

## Overview

This week introduced the idea of simulating a quantum computer as a stack machine.

The simulator represents the quantum workspace as a NumPy array and performs four main operations:

- `pushQubit(...)` - pushes a new qubit onto the stack using the Kronecker product
- `applyGate(...)` - applies a gate to one or more qubits using matrix multiplication
- `tosQubit(...)` - moves a named qubit to the top of the stack
- `measureQubit(...)` - measures and removes a qubit from the stack

The code also includes `probQubit(...)`, which is useful in a simulator for checking qubit measurement probabilities before actually measuring them.

---

## How to Run

From inside the `week7` folder:

```bash
python3 quantum_part1.py
```

---

## What the Program Demonstrates

The program includes four built-in demonstrations:

1. **Push + Hadamard gate**
   - starts with a qubit in state 0
   - applies the Hadamard gate
   - shows that the probabilities become 50% for 0 and 50% for 1

2. **Moving qubits in the stack**
   - demonstrates how a named qubit can be moved to the top of the stack

3. **Measurement**
   - calculates and displays probabilities
   - measures qubits and collapses the workspace

4. **Toffoli gate sample**
   - applies a 3-qubit Toffoli gate
   - produces sample measurement outputs similar to a truth-table style test

---

## Key Ideas Learned

- A quantum computer can be represented as a stack machine
- The workspace grows exponentially as qubits are added
- Gates are applied through matrix multiplication
- Qubits must sometimes be moved before gates are applied
- Measurement collapses the state and removes the measured qubit
- Multi-qubit gates, such as the Toffoli gate, are important for useful quantum computations

---

## Results Table



| Demo Section | What Was Tested | Example Observation |
|--------------|------------------|---------------------|
| Push + H gate | Single qubit superposition | Probabilities became approximately [0.5, 0.5] |
| Move to TOS | Reordering qubits | Workspace ordering changed after moving Q1 |
| Measurement | Measuring Q1 and Q2 | Output returned binary values and collapsed the state |
| Toffoli test | Multi-qubit logic behaviour | Produced a sequence of binary outputs |

---

## Conclusion

This exercise showed how a basic quantum computer simulator can be built using only NumPy operations. The tutorial demonstrated that the main quantum instructions can be implemented with a small set of linear algebra operations: Kronecker product, matrix multiplication, axis swapping and norm calculation.

The simulator provides a practical way to understand how qubits are stored, manipulated and measured, and it gives a useful programming-level introduction to quantum computing without requiring advanced quantum physics.
