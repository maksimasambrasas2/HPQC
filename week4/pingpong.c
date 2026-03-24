#include <stdio.h>
#include <stdlib.h>
#include <mpi.h>

int main(int argc, char *argv[]) {
    int rank;
    int counter = 0;
    int num_pings;

    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);

    num_pings = atoi(argv[1]);

    double start = MPI_Wtime();

    while (counter < num_pings) {
        if (rank == 0) {
            MPI_Send(&counter, 1, MPI_INT, 1, 0, MPI_COMM_WORLD);
            MPI_Recv(&counter, 1, MPI_INT, 1, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
        } else {
            MPI_Recv(&counter, 1, MPI_INT, 0, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
            counter++;
            MPI_Send(&counter, 1, MPI_INT, 0, 0, MPI_COMM_WORLD);
        }
    }

    double end = MPI_Wtime();

    if (rank == 0) {
        double elapsed = end - start;
        printf("Final counter: %d\n", counter);
        printf("Elapsed time: %f\n", elapsed);
        printf("Average time per ping: %f\n", elapsed / num_pings);
    }

    MPI_Finalize();
    return 0;
}
