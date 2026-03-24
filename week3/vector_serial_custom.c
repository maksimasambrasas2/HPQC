#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Usage: ./vector_serial_custom <vector_size>\n");
        return 1;
    }

    int n = atoi(argv[1]);
    long long sum = 0;

    int *vector = malloc(n * sizeof(int));
    if (vector == NULL) {
        printf("Memory allocation failed\n");
        return 1;
    }

    clock_t start = clock();

    for (int i = 0; i < n; i++) {
        vector[i] = i + 1;              // non-trivial: vector contains 1,2,3,...
    }

    for (int i = 0; i < n; i++) {
        sum += vector[i] * vector[i];   // non-trivial operation: sum of squares
    }

    clock_t end = clock();

    double runtime = (double)(end - start) / CLOCKS_PER_SEC;

    printf("Vector size: %d\n", n);
    printf("Sum of squares: %lld\n", sum);
    printf("Internal runtime: %.6f seconds\n", runtime);

    free(vector);
    return 0;
}
