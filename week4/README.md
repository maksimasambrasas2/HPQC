# Week 4: MPI Communications

## Files Included

- `comm_test_mpi.c` - original MPI communication test program
- `comm_test_modular.c` - functionalised version of communication test
- `comm_send_types.c` - program testing different MPI send types
- `pingpong.c` - latency measurement program
- `pingpong_array.c` - bandwidth measurement program
- `vector_collective.c` - vector addition using collective communication

---

## Part 1: Demonstrating Communications

### Step 1: Running the original program

The `comm_test_mpi.c` program was compiled and executed using different numbers of processes:

```bash
mpicc comm_test_mpi.c -o bin/comm_test
mpirun --oversubscribe -np 2 bin/comm_test
mpirun --oversubscribe -np 4 bin/comm_test
mpirun --oversubscribe -np 8 bin/comm_test
```

### Observations

- The order of output messages changes between runs  
- Processes do not execute in a fixed order  
- This demonstrates that MPI programs run in parallel and are not strictly sequential  

---

### Step 2: Functionalised version

The original code was split into smaller functions:
- `send_message()` handles sending data  
- `receive_messages()` handles receiving data  

This makes the program:
- easier to read  
- easier to debug  
- easier to extend  

---

### Step 3: MPI Send Types

The following MPI send variants were tested:

- `MPI_Ssend()` (synchronous send)  
- `MPI_Bsend()` (buffered send)  
- `MPI_Rsend()` (ready send)  
- `MPI_Isend()` (non-blocking send)  

### Observations

- `MPI_Ssend()` is reliable but slower due to synchronization  
- `MPI_Bsend()` requires buffer management  
- `MPI_Rsend()` can cause errors if the receive is not ready  
- `MPI_Isend()` allows non-blocking communication but requires careful handling  

### Conclusion

`MPI_Ssend()` is the most reliable and predictable for this type of program.

---

### Step 4: Timing communications

Timing was implemented using:

```c
double start = MPI_Wtime();
/* communication */
double end = MPI_Wtime();
```

### Observations

- Execution times are extremely small  
- Results vary significantly between runs  
- Variability is often comparable to measured time  

---

## Part 2: Latency and Bandwidth

### Step 1: Ping Pong Program

The `pingpong.c` program sends a message back and forth between two processes.

### How it works

- Root sends a counter to client  
- Client increments and sends back  
- This repeats for many iterations  

### Execution example

```bash
mpicc pingpong.c -o bin/pingpong
mpirun -np 2 bin/pingpong 1000
```

### Observations

- Increasing number of pings improves accuracy  
- Results converge as number of iterations increases  

### Conclusion

This program measures **latency** — the time for a message to travel between processes.

---

### Step 3: Bandwidth Program

The `pingpong_array.c` program sends arrays instead of single integers.

### Execution example

```bash
mpicc pingpong_array.c -o bin/pingpong_array
mpirun -np 2 bin/pingpong_array 1000 100
mpirun -np 2 bin/pingpong_array 1000 10000
```

### Observations

- Small message sizes → latency dominates  
- Large message sizes → bandwidth dominates  

### Conclusion

- Latency = fixed communication cost  
- Bandwidth = data transfer rate  

---

## Part 3: Collective Communications

### Program: vector_collective.c

This program uses `MPI_Reduce()` to sum values across processes.

### How it works

- Each process computes a local sum  
- `MPI_Reduce()` combines all local sums into a global sum  

### Execution example

```bash
mpicc vector_collective.c -o bin/vector_collective
mpirun -np 4 bin/vector_collective 1000
```

---

### Observations

- Collective operations simplify code  
- `MPI_Reduce()` replaces manual send/receive loops  
- Communication is more efficient than point-to-point methods  

---

## Overall Conclusions

- MPI allows multiple processes to run simultaneously  
- Communication between processes is not ordered and can vary between runs  
- Different send methods have different trade-offs:
  - synchronous = safe
  - non-blocking = faster but complex  
- Latency dominates small messages  
- Bandwidth dominates large messages  
- Collective communication (`MPI_Reduce`) is more efficient than manual messaging  

---

## Summary

This exercise demonstrated:
- MPI communication behaviour  
- differences between send methods  
- how to measure latency and bandwidth  
- advantages of collective communication over point-to-point communication  
