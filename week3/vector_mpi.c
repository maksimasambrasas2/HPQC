#include <stdio.h>
#include <stdlib.h>
#include <mpi.h>

int main(int argc, char *argv[]) {
    int rank, size;
    int n;

    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    if (argc != 2) {
        if (rank == 0) {
            printf("Usage: mpirun -np <num_processes> ./vector_mpi <vector_size>\n");
        }
        MPI_Finalize();
        return 1;
    }

    n = atoi(argv[1]);

    int chunk = n / size;
    int remainder = n % size;

    int start, end;
    if (rank < remainder) {
        start = rank * (chunk + 1);
        end = start + chunk + 1;
    } else {
        start = rank * chunk + remainder;
        end = start + chunk;
    }

    double start_time = MPI_Wtime();

    long long local_sum = 0;
    for (int i = start; i < end; i++) {
        int value = i + 1;                  // values 1,2,3,...
        local_sum += (long long)value * value;
    }

    long long global_sum = 0;
    MPI_Reduce(&local_sum, &global_sum, 1, MPI_LONG_LONG, MPI_SUM, 0, MPI_COMM_WORLD);

    double end_time = MPI_Wtime();

    if (rank == 0) {
        printf("Vector size: %d\n", n);
        printf("Sum of squares: %lld\n", global_sum);
        printf("Internal runtime: %.6f seconds\n", end_time - start_time);
    }

    MPI_Finalize();
    return 0;
}
