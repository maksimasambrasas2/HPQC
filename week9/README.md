# Week 9: Program Your Own Quantum Computer – Part 3 (GPUs)

## Files Included

- grover_gpu_part3.py - PyTorch implementation of the quantum computer simulator and Grover's search

---

## Overview

This week extended the quantum computer simulator developed in previous weeks by replacing NumPy operations with PyTorch operations. This allows the simulator to run on either a CPU or a GPU depending on hardware availability.

The aim of this task was to demonstrate how quantum simulation workloads can be accelerated using GPU-style parallel computation. Although GPU acceleration was not available on the Frank cluster, the implementation was successfully tested on CPU using PyTorch.

---

## How to Run

From inside the week9 folder:

source ~/torch_env/bin/activate
python3 grover_gpu_part3.py

---

## What the Program Does

The program:

1. Checks if a GPU is available using PyTorch
2. Initializes the quantum workspace on the selected device
3. Implements Grover's search algorithm
4. Prints probability updates for convergence
5. Measures the final result
6. Benchmarks runtime on the current device
7. Performs an additional CPU comparison run

---

## Results Table

| Test | Device Used | Measured Result | Runtime (s) | Notes |
|------|-------------|-----------------|-------------|-------|
| Main Grover run | CPU | 11111101 | 0.047196 | PyTorch CPU execution (no GPU available) |
| CPU comparison  | CPU | 11111101 | 0.041768 | Second run for comparison |

---

## Probability Convergence Table

| Iteration | Probability of 0 | Probability of 1 |
|-----------|------------------|------------------|
| 1 | 0.48449704 | 0.51550300 |
| 2 | 0.45445636 | 0.54554370 |
| 3 | 0.41174805 | 0.58825190 |
| 4 | 0.35903102 | 0.64096900 |
| 5 | 0.29958710 | 0.70041290 |
| 6 | 0.23711738 | 0.76288265 |
| 7 | 0.17551060 | 0.82448940 |
| 8 | 0.11860219 | 0.88139780 |
| 9 | 0.06993513 | 0.93006486 |
| 10 | 0.03253920 | 0.96746080 |
| 11 | 0.00874253 | 0.99125750 |
| 12 | 0.00002658 | 0.99997340 |

---

## Result Summary

| Number of Qubits | Expected Result | Measured Result | Correct? |
|------------------|-----------------|-----------------|----------|
| 8 | 11111101 | 11111101 | Yes |

---

## Discussion

The results show clear convergence of probabilities toward the correct solution. Initially, the probability of measuring a 1 is close to 0.5, indicating a uniform superposition. As Grover's iterations proceed, the probability of the correct state increases steadily, reaching approximately 0.99997 in the final iteration.

The final measured result matches the expected solution 11111101, confirming that the implementation of Grover’s algorithm is correct.

Although GPU acceleration was not available in this environment, the PyTorch implementation demonstrates how the simulator can be adapted to run on different hardware with minimal code changes. The runtime for both executions was very low (around 0.04 seconds), which is expected for a small number of qubits (n = 8).

---

## Key Learnings

- PyTorch can replace NumPy for quantum simulator operations
- The workspace can be stored entirely on the selected device
- GPU acceleration is well-suited for quantum simulation workloads
- Grover's algorithm successfully amplifies the probability of the correct solution
- Measurement remains probabilistic, but high probability ensures correctness
- Virtual environments are useful for managing dependencies on shared systems

---

## Conclusion

This exercise demonstrated how a quantum computer simulator can be extended to use PyTorch for potential GPU acceleration. While GPU execution was not possible on the Frank cluster, the implementation still successfully demonstrated the functionality and flexibility of the approach.

The transition from NumPy to PyTorch required only small changes to the code, showing that quantum simulation frameworks can be easily adapted for high-performance computing environments. This highlights the potential for future integration with dedicated quantum hardware or GPU-accelerated simulation platforms.
