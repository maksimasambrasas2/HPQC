#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Usage: ./write_file <num_lines>\n");
        return 1;
    }

    int num_lines = atoi(argv[1]);
    FILE *fp = fopen("../data/test_c.txt", "w");

    if (fp == NULL) {
        printf("Error opening file.\n");
        return 1;
    }

    clock_t start_time = clock();

    for (int i = 0; i < num_lines; i++) {
        fprintf(fp, "This is line %d\n", i);
    }

    clock_t end_time = clock();

    fclose(fp);

    double run_time = (double)(end_time - start_time) / CLOCKS_PER_SEC;

    printf("Wrote %d lines to ../data/test_c.txt\n", num_lines);
    printf("Internal runtime: %.6f seconds\n", run_time);

    return 0;
}
