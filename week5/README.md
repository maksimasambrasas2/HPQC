# Week 5: Communicators and Topologies

## Files Included

- `string_wave_custom.c` - serial string oscillation program with command-line arguments
- `animate_line_file_custom.py` - Python animation script with command-line arguments
- `string_wave_mpi.c` - MPI parallel version of the string oscillation program
- `string_wave_improved.c` - improved physical model using spring-like motion

---

## Part 1: Serial Code

### Compilation
```bash
gcc week5/string_wave_custom.c -o bin/string_wave_custom -lm
```

### Example Run
```bash
./bin/string_wave_custom 50 100 data/string_wave_custom.csv
python3 week5/animate_line_file_custom.py data/string_wave_custom.csv data/string_wave_custom.gif
```

### What was changed
- removed hard-coded sample count
- removed hard-coded cycle count
- removed hard-coded output file path
- updated the program to accept command-line arguments

### Results Table

| Samples | Cycles | Real Time (s) | Notes |
|---------|--------|---------------|-------|
| 50      | 100    | 0.008         | Very fast, small problem |
| 500     | 100    | 0.023         | Moderate increase |
| 5000    | 100    | 0.188         | Significant scaling |

---

## Part 2: Parallel Code

### Compilation
```bash
mpicc week5/string_wave_mpi.c -o bin/string_wave_mpi -lm
```

### Example Run
```bash
mpirun --oversubscribe -np 4 ./bin/string_wave_mpi 50 100 data/string_wave_mpi.csv
python3 week5/animate_line_file_custom.py data/string_wave_mpi.csv data/string_wave_mpi.gif
```

### Parallel Strategy
- the string was split into chunks across processes
- each process updated its local points
- neighbouring processes exchanged boundary values
- the root process gathered results and wrote them to file

### Aggregation Strategy
- only the root process writes to the CSV file
- results are gathered using `MPI_Gatherv()`

### Results Table

| Processes | Samples | Cycles | Real Time (s) | Notes |
|-----------|---------|--------|---------------|-------|
| 2         | 500     | 100    | 0.085         | Overhead dominates |
| 4         | 500     | 100    | 0.036         | Faster than 2 processes |
| 4         | 5000    | 100    | 0.057         | Much better scaling |

---

## Serial vs Parallel Comparison

| Samples | Cycles | Serial Time (s) | Parallel Time (s) | Faster Version |
|---------|--------|-----------------|-------------------|----------------|
| 50      | 100    | 0.008           | 0.085             | Serial |
| 500     | 100    | 0.023           | 0.036             | Serial |
| 5000    | 100    | 0.188           | 0.057             | Parallel |

### Discussion
For small problem sizes, the serial version is expected to perform better because MPI communication adds overhead. For larger problems, the parallel version becomes more viable because the work is divided across multiple processes.

---

## Part 3: Improved Model

### Compilation
```bash
gcc week5/string_wave_improved.c -o bin/string_wave_improved -lm
```

### Example Run
```bash
./bin/string_wave_improved 50 200 1.0 1.0 data/string_wave_improved.csv
python3 week5/animate_line_file_custom.py data/string_wave_improved.csv data/string_wave_improved.gif
```

### What was improved
- added position, velocity and acceleration arrays
- introduced a spring-like force between neighbouring points
- used parameters for spring constant `k` and mass `m`
- produced a more realistic oscillation than the original shift-based update

### Results Table

| Samples | Cycles | k | m | Real Time (s) | Notes |
|---------|--------|---|---|---------------|-------|
| 50      | 200    | 1.0 | 1.0 | 0.014 | Smooth oscillation |
| 100     | 200    | 1.0 | 1.0 | 0.010 | Efficient computation |
| 100     | 200    | 2.0 | 1.0 | 0.018 | Stronger oscillation, slightly slower |

---

## Conclusions

This week began with a simple serial model of oscillations on a string and progressively developed it into a more flexible and more realistic simulation.

The serial code was improved by removing hard-coded values and allowing the user to specify the number of samples, number of cycles and output file path from the command line.

The MPI version parallelised the update of the string by splitting the data across processes. The time evolution itself remained sequential, because each cycle depends on the previous cycle, but the work within each cycle was distributed. Communication between neighbouring processes was necessary to exchange edge values.

The aggregation strategy used root-only file output, which is safer than allowing multiple processes to write to the same file simultaneously.

The improved model used a spring-based approach with position, velocity and acceleration, producing more realistic string motion than the original simple copy/update rule.

Overall, this exercise showed that parallelisation is not always beneficial for small tasks, but becomes more useful as the size of the simulation increases.
