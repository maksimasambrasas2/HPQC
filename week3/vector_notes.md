# Notes on vector programs

## Serial version

The serial version creates a vector of numbers from 1 up to n. It then calculates the sum of the squares of all elements in the vector.

### Steps
1. Read the input value n
2. Allocate memory for the vector
3. Fill the vector with values 1 to n
4. Loop through the vector and calculate the sum of squares
5. Measure and print the runtime
6. Free the allocated memory

## Parallel MPI version

The MPI version divides the work between multiple processes.

### Steps
1. Start MPI
2. Read the input value n
3. Divide the vector into chunks
4. Assign each chunk to one MPI process
5. Each process calculates the sum of squares for its own chunk
6. Use MPI_Reduce to add all local sums together
7. Root process prints the final result and runtime
8. End MPI

## Comparison

The serial version does all work in one process.

The MPI version shares the work across multiple processes. This can reduce real runtime for sufficiently large input sizes, although for small inputs the MPI overhead can make it slower.
