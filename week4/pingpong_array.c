#include <stdio.h>
#include <stdlib.h>
#include <mpi.h>

int main(int argc, char *argv[]) {
    int rank;
    int num_pings = atoi(argv[1]);
    int size = atoi(argv[2]);

    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);

    int *array = malloc(size * sizeof(int));

    double start = MPI_Wtime();

    for (int i = 0; i < num_pings; i++) {
        if (rank == 0) {
            MPI_Send(array, size, MPI_INT, 1, 0, MPI_COMM_WORLD);
            MPI_Recv(array, size, MPI_INT, 1, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
        } else {
            MPI_Recv(array, size, MPI_INT, 0, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
            MPI_Send(array, size, MPI_INT, 0, 0, MPI_COMM_WORLD);
        }
    }

    double end = MPI_Wtime();

    if (rank == 0) {
        printf("Size: %d ints\n", size);
        printf("Time: %f\n", end - start);
    }

    free(array);
    MPI_Finalize();
    return 0;
}
