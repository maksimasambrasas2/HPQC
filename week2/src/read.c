#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    FILE *fp = fopen("../data/test_c.txt", "r");

    if (fp == NULL) {
        printf("Error opening file.\n");
        return 1;
    }

    clock_t start_time = clock();

    fseek(fp, 0, SEEK_END);
    long file_size = ftell(fp);
    rewind(fp);

    char *buffer = malloc(file_size + 1);
    if (buffer == NULL) {
        printf("Memory allocation failed.\n");
        fclose(fp);
        return 1;
    }

    fread(buffer, 1, file_size, fp);
    buffer[file_size] = '\0';

    clock_t end_time = clock();

    fclose(fp);
    free(buffer);

    double run_time = (double)(end_time - start_time) / CLOCKS_PER_SEC;

    printf("Read %ld bytes from ../data/test_c.txt\n", file_size);
    printf("Internal runtime: %.6f seconds\n", run_time);

    return 0;
}
