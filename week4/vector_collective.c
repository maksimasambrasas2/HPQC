#include <stdio.h>
#include <stdlib.h>
#include <mpi.h>

int main(int argc, char *argv[]) {
    int rank, size;
    int n = atoi(argv[1]);

    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    int local_n = n / size;
    int *data = malloc(local_n * sizeof(int));

    for (int i = 0; i < local_n; i++) {
        data[i] = i + rank * local_n;
    }

    int local_sum = 0;
    for (int i = 0; i < local_n; i++) {
        local_sum += data[i];
    }

    int global_sum;
    MPI_Reduce(&local_sum, &global_sum, 1, MPI_INT, MPI_SUM, 0, MPI_COMM_WORLD);

    if (rank == 0) {
        printf("Global sum: %d\n", global_sum);
    }

    free(data);
    MPI_Finalize();
    return 0;
}
