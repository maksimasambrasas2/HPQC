#include <stdio.h>
#include <mpi.h>

int main(int argc, char *argv[]) {
    int rank, size;

    MPI_Init(&argc, &argv);                  // Start MPI
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);    // Get this process rank
    MPI_Comm_size(MPI_COMM_WORLD, &size);    // Get total number of processes

    printf("Hello from process %d of %d\n", rank, size);

    MPI_Finalize();                          // End MPI
    return 0;
}
