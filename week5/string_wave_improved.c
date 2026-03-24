#include <stdio.h>
#include <stdlib.h>
#include <math.h>

typedef struct {
    int samples;
    int cycles;
    double k;
    double m;
    char output_file[256];
} Args;

Args check_args(int argc, char *argv[]) {
    Args args;

    if (argc != 6) {
        fprintf(stderr, "Usage: ./string_wave_improved <samples> <cycles> <k> <m> <output_file>\n");
        exit(1);
    }

    args.samples = atoi(argv[1]);
    args.cycles = atoi(argv[2]);
    args.k = atof(argv[3]);
    args.m = atof(argv[4]);
    snprintf(args.output_file, sizeof(args.output_file), "%s", argv[5]);

    return args;
}

int main(int argc, char *argv[]) {
    Args args = check_args(argc, argv);

    double dt = 0.01;
    double *x = malloc(args.samples * sizeof(double));
    double *v = malloc(args.samples * sizeof(double));
    double *a = malloc(args.samples * sizeof(double));

    FILE *fp = fopen(args.output_file, "w");
    fprintf(fp, "cycle,index,position\n");

    for (int i = 0; i < args.samples; i++) {
        x[i] = sin(2.0 * M_PI * i / args.samples);
        v[i] = 0.0;
        a[i] = 0.0;
    }

    for (int c = 0; c < args.cycles; c++) {
        for (int i = 0; i < args.samples; i++) {
            fprintf(fp, "%d,%d,%.6f\n", c, i, x[i]);
        }

        for (int i = 1; i < args.samples - 1; i++) {
            double force = args.k * (x[i - 1] - x[i]) + args.k * (x[i + 1] - x[i]);
            a[i] = force / args.m;
        }

        for (int i = 1; i < args.samples - 1; i++) {
            v[i] += a[i] * dt;
            x[i] += v[i] * dt;
        }

        x[0] = 0.0;
        x[args.samples - 1] = 0.0;
        v[0] = 0.0;
        v[args.samples - 1] = 0.0;
    }

    fclose(fp);
    free(x);
    free(v);
    free(a);

    return 0;
}
