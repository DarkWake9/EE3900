#include <stdio.h>
#include <math.h>
#include <time.h>
#include <stdlib.h>
#include "fftw3.h"

int main()
{
    srand(time(NULL));
    clock_t fb, fe;
    FILE *fp1 = fopen("fftw.txt", "w");
    int N;
    for (N=1;N<=1000;N++)
    {
    fftwl_complex in[N], out[N];
    fftwl_plan p1, q;

    for (int i = 0; i < N; i++) {
        in[i][0] = rand()/RAND_MAX;
        in[i][1] = rand()/RAND_MAX;
    }

    p1 = fftwl_plan_dft_1d(N, in, out, FFTW_FORWARD, FFTW_ESTIMATE);
    q = fftwl_plan_dft_1d(N, in, out, FFTW_BACKWARD, FFTW_ESTIMATE);
    fb = clock();
    fftwl_execute(p1);
    fftwl_execute(q);
    fe = clock();
    fftwl_destroy_plan(p1);
    fftwl_destroy_plan(q);
    fprintf(fp1, "%lf\n", 1000*(double)(fe - fb)/CLOCKS_PER_SEC);
    }
    fclose(fp1);
    return 0;
}
