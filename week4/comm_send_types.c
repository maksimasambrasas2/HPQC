#include <stdio.h>
#include <mpi.h>

int main(int argc, char *argv[]) {
    int rank;
    MPI_Status status;

    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);

    int msg = rank;

    if (rank == 0) {
        MPI_Recv(&msg, 1, MPI_INT, 1, 0, MPI_COMM_WORLD, &status);
        printf("Received: %d\n", msg);
    } else {
        // Try changing between these:

        MPI_Ssend(&msg, 1, MPI_INT, 0, 0, MPI_COMM_WORLD);   // synchronous
        // MPI_Bsend(...)
        // MPI_Rsend(...)
        // MPI_Isend(...)

        printf("Sent: %d\n", msg);
    }

    MPI_Finalize();
    return 0;
}

double start = MPI_Wtime();

// send or recv

double end = MPI_Wtime();
printf("Rank %d took %f seconds\n", rank, end - start);
