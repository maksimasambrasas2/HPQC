#include <stdio.h>
#include <mpi.h>

void send_message(int rank) {
    int msg = rank;
    MPI_Send(&msg, 1, MPI_INT, 0, 0, MPI_COMM_WORLD);
}

void receive_messages(int size) {
    int msg;
    MPI_Status status;

    for (int i = 1; i < size; i++) {
        MPI_Recv(&msg, 1, MPI_INT, i, 0, MPI_COMM_WORLD, &status);
        printf("Root received %d\n", msg);
    }
}

int main(int argc, char *argv[]) {
    int rank, size;

    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    if (rank == 0) {
        receive_messages(size);
    } else {
        send_message(rank);
    }

    MPI_Finalize();
    return 0;
}
