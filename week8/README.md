# Week 8: Program Your Own Quantum Computer – Part 2 (Grover's Search)

## Files Included

- `grover_part2.py` - Python implementation of Grover's search based on the tutorial

---

## Overview

This week extended the basic quantum stack-machine simulator from Part 1 and applied it to Grover's search.

Grover's search is a quantum algorithm that can search a space of size `2^N` in approximately `O(2^(N/2))` time, giving a quadratic speedup over a naive classical search.

The program implements:

- `zero_booleanOracle(...)`
- `zero_phaseOracle(...)`
- `sample_phaseOracle(...)`
- `groverSearch(...)`

The tutorial example searches for a bitstring where all qubits except qubit 1 are one, which should produce the solution:

```text
111101
```

---

## How to Run

From inside the `week8` folder:

```bash
python3 grover_part2.py
```

---

## What the Program Demonstrates

The program performs the following steps:

1. Creates `n` qubits in equal superposition using the Hadamard-style initialization
2. Applies the sample phase oracle
3. Applies Hadamard gates
4. Applies the zero phase oracle
5. Applies Hadamard gates again
6. Repeats the process for the optimal number of Grover iterations
7. Measures all qubits to obtain the final result

The program also prints the probability distribution for qubit 0 during each iteration so that convergence can be observed.

---

## Key Ideas Learned

- Grover's search uses amplitude amplification
- The phase oracle flips the sign of the solution state's amplitude
- The zero phase oracle helps reflect the state vector in the correct direction
- Repeated Grover iterations gradually increase the probability of measuring the correct solution
- The result is not guaranteed with 100% certainty, so in principle the search may need to be repeated

---

## Results Table

Fill this in with your own output after running the program.

| Iteration | Probability of 0 | Probability of 1 |
|-----------|------------------|------------------|
| 1         | 0.43945313       | 0.56054687       |
| 2         | 0.33325958       | 0.66674042       |
| 3         | 0.20755294       | 0.79244706       |
| 4         | 0.09326882       | 0.90673118       |
| 5         | 0.01853182       | 0.98146818       |

### Final Measurement

| Number of Qubits | Expected Result | Measured Result | Correct? |
|------------------|-----------------|-----------------|----------|
| 6                | 111101          | 111101          | Yes      |

---

## Example Discussion

As Grover's algorithm progressed, the probability of measuring the correct value for qubit 0 increased while the probability of measuring the wrong value decreased. This showed that the algorithm was successfully amplifying the amplitude of the correct solution.

The final measured result should be close to the expected tutorial answer `111101`. Because measurement is probabilistic, a different answer may occasionally appear, but the correct result should be much more likely after the optimal number of iterations.

---

## Conclusion

This exercise showed how a quantum search algorithm can be built using the stack-machine simulator from Part 1. By combining phase oracles with repeated Grover iterations, the simulator gradually increased the amplitude of the correct solution state.

The tutorial demonstrated that the difficult part of quantum computing is often not performing the computation itself, but extracting the correct result through measurement. Grover's search provided a concrete example of how quantum algorithms can offer a speedup over classical methods.
