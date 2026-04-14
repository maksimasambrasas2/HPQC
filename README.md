# HPQC

This repository contains coursework for the High Performance and Quantum Computing module. It covers topics ranging from performance benchmarking and parallel computing with MPI to quantum computing simulations using Python and PyTorch.

---

## Repository Structure

- week2/ - Topic 2: Performance and Parallelism  
- week3/ - Topic 3: Introduction to MPI  
- week4/ - Topic 4: MPI Communications  
- week5/ - Topic 5: Parallel Modelling (String Oscillations)  
- week7/ - Topic 7: Quantum Computer Simulator (Part 1)  
- week8/ - Topic 8: Grover’s Search (Part 2)  
- week9/ - Topic 9: GPU Simulation with PyTorch (Part 3)  

Each weekly folder contains the code, results, and documentation relevant to that topic.

---

## Week 2: Performance and Parallelism

Week 2 focuses on benchmarking program performance in C and Python, including:

- Using the Linux `time` command
- Measuring internal execution time
- Comparing interpreted (Python) vs compiled (C) programs
- File input/output benchmarking
- Observing how runtime scales with input size

See `week2/README.md` for detailed results and analysis.

---

## Week 3: Introduction to MPI

Week 3 introduces Message Passing Interface (MPI) programming:

- MPI Hello World implementation
- Communication between root and worker processes
- Understanding ranks and communicator size
- Serial vs parallel vector operations
- Performance comparison between implementations

See `week3/README.md` for full explanations and results.

---

## Week 4: MPI Communications

Week 4 explores different MPI communication strategies:

- Refactoring code into modular functions
- Comparing communication methods:
  - MPI_Send
  - MPI_Ssend
  - MPI_Bsend
  - MPI_Isend
- Observing differences in behaviour and reliability
- Benchmarking communication overhead

See `week4/README.md` for implementation details and discussion.

---

## Week 5: Parallel Modelling (Oscillations on a String)

Week 5 applies parallel computing to a physics-based simulation:

- Serial simulation of a vibrating string in C
- Removal of hard-coded parameters
- Parallelisation using MPI
- Domain decomposition across processes
- Communication between neighbouring nodes
- Performance benchmarking and scalability analysis

See `week5/README.md` for results and evaluation.

---

## Week 7: Quantum Computer Simulator (Part 1)

Week 7 introduces a custom quantum computer simulator:

- Implementation of a quantum stack machine
- Core operations:
  - pushQubit
  - applyGate
  - tosQubit
  - measureQubit
- Simulation of quantum states using vectors
- Use of linear algebra (Kronecker products and matrix multiplication)
- Implementation of basic quantum gates (X, H, Z, etc.)

See `week7/README.md` for full implementation details.

---

## Week 8: Grover’s Search Algorithm (Part 2)

Week 8 builds on the simulator to implement Grover’s search:

- Boolean and phase oracles
- Amplitude amplification
- Iterative probability improvement
- Measurement of quantum states
- Demonstration of quadratic speedup over classical search

The algorithm successfully converges to the expected solution with high probability.

See `week8/README.md` for results and convergence analysis.

---

## Week 9: GPU Simulation with PyTorch (Part 3)

Week 9 adapts the simulator to run using PyTorch:

- Replacement of NumPy with PyTorch tensor operations
- Device selection (CPU vs GPU)
- Execution of Grover’s algorithm using PyTorch
- Runtime benchmarking
- Use of virtual environments for dependency management

Although GPU acceleration was not available on the cluster, the implementation successfully demonstrated CPU execution and maintained correct functionality.

See `week9/README.md` for full results and performance analysis.

---

## Summary

This repository demonstrates:

- Performance analysis of programs
- Parallel computing using MPI
- Implementation of numerical simulations
- Development of a custom quantum computer simulator
- Implementation of a quantum search algorithm
- Adaptation of code for high-performance computing using PyTorch

The progression across weeks reflects a transition from classical high-performance computing techniques to quantum computing concepts and simulation.

---

## Author

Maksimas Ambrasas  
BSc Physics with Data Analytics  
Dublin City University
