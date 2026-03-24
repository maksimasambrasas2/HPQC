# Week 3: Introduction to MPI

## Files Included
- `hello_mpi.c` - MPI Hello World program
- `hello_serial.c` - serial comparison version of Hello World
- `proof_notes.md` - explanation of the structure and logic of `proof.c`
- `vector_serial_custom.c` - modified serial vector program using a non-trivial mathematical operation
- `vector_mpi.c` - MPI parallel version of the vector program
- `vector_notes.md` - notes explaining the serial and parallel vector programs

## How to Run

### Compile programs
```bash
mpicc week3/hello_mpi.c -o bin/hello_mpi
gcc week3/hello_serial.c -o bin/hello_serial
gcc week3/vector_serial_custom.c -o bin/vector_serial_custom
mpicc week3/vector_mpi.c -o bin/vector_mpi

Run programs
mpirun -np 4 bin/hello_mpi
./bin/hello_serial
./bin/vector_serial_custom 10
mpirun -np 4 bin/vector_mpi 10
Benchmark examples
time mpirun -np 4 bin/hello_mpi
time ./bin/hello_serial
time ./bin/vector_serial_custom 100000
time mpirun -np 4 bin/vector_mpi 100000
Summary

In this topic, MPI was introduced through a Hello World example, examination of the proof.c message-passing program, and a vector summation task.

The MPI Hello World program demonstrated that multiple processes can run simultaneously, each with its own rank. The proof.c notes explain how root and client processes communicate using MPI_Send and MPI_Recv.

The serial vector program calculates the sum of squares of vector elements in a single process. The MPI version divides the vector into chunks, gives each chunk to a different process, calculates local partial sums, and combines them using MPI_Reduce.

This demonstrates the key MPI idea of splitting work across processes and then combining the results.
