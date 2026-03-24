#include <stdio.h>
#include <stdlib.h>
#include <math.h>

typedef struct {
    int samples;
    int cycles;
    char output_file[256];
} Args;

Args check_args(int argc, char *argv[]) {
    Args args;

    if (argc != 4) {
        fprintf(stderr, "Usage: ./string_wave_custom <samples> <cycles> <output_file>\n");
        exit(1);
    }

    args.samples = atoi(argv[1]);
    args.cycles = atoi(argv[2]);
    snprintf(args.output_file, sizeof(args.output_file), "%s", argv[3]);

    return args;
}

void initialise_positions(double *positions, int samples) {
    for (int i = 0; i < samples; i++) {
        positions[i] = sin(2.0 * M_PI * i / samples);
    }
}

void update_positions(double *old_pos, double *new_pos, int samples) {
    for (int i = 1; i < samples - 1; i++) {
        new_pos[i] = old_pos[i + 1];
    }
    new_pos[0] = 0.0;
    new_pos[samples - 1] = 0.0;
}

void write_frame(FILE *fp, double *positions, int samples, int cycle) {
    for (int i = 0; i < samples; i++) {
        fprintf(fp, "%d,%d,%.6f\n", cycle, i, positions[i]);
    }
}

int main(int argc, char *argv[]) {
    Args args = check_args(argc, argv);

    double *positions = malloc(args.samples * sizeof(double));
    double *new_positions = malloc(args.samples * sizeof(double));

    if (positions == NULL || new_positions == NULL) {
        fprintf(stderr, "Memory allocation failed.\n");
        return 1;
    }

    FILE *fp = fopen(args.output_file, "w");
    if (fp == NULL) {
        fprintf(stderr, "Could not open output file.\n");
        free(positions);
        free(new_positions);
        return 1;
    }

    fprintf(fp, "cycle,index,position\n");

    initialise_positions(positions, args.samples);

    for (int c = 0; c < args.cycles; c++) {
        write_frame(fp, positions, args.samples, c);
        update_positions(positions, new_positions, args.samples);

        for (int i = 0; i < args.samples; i++) {
            positions[i] = new_positions[i];
        }
    }

    fclose(fp);
    free(positions);
    free(new_positions);

    return 0;
}
