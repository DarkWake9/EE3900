#include <stdio.h>
#include <stdbool.h>
#include <math.h>
#include <stdlib.h>
#include <complex.h>
#include <time.h>
#define EPS 1e-6

int N;

complex *myfft(int n, complex *a) {
	if (n == 1) return a;
	complex *g = (complex *)malloc(n/2*sizeof(complex));
	complex *h = (complex *)malloc(n/2*sizeof(complex));
	for (int i = 0; i < n; i++) { 
		if (i%2) h[i/2] = a[i];
		else g[i/2] = a[i];
	}
	g = myfft(n/2, g);
	h = myfft(n/2, h);
	for (int i = 0; i < n; i++) a[i] = g[i%(n/2)] + cexp(-I*2*M_PI*i/n)*h[i%(n/2)];
	free(g); free(h);
	return a;
}

complex *myifft(int n, complex *a) { 
	if (n == 1) return a;
	complex *g = (complex *)malloc(n/2*sizeof(complex));
	complex *h = (complex *)malloc(n/2*sizeof(complex));
	for (int i = 0; i < n; i++) { 
		if (i%2) h[i/2] = a[i];
		else g[i/2] = a[i];
	}
	g = myifft(n/2, g);
	h = myifft(n/2, h);
	for (int i = 0; i < n; i++) {
		a[i] = g[i%(n/2)] + cexp(I*2*M_PI*i/n)*h[i%(n/2)];
		a[i] /= 2;
	}
	free(g); free(h);
	return a;
}

complex *convolve(complex *h, complex *x, int n) { 
	complex *a = (complex *)calloc(n, sizeof(complex));
	for (int i = 0; i < n; i++) for (int j = 0; j <= i; j++) if (j < N && i - j < N) a[i] += h[j]*x[i - j];
	return a;
}

int main() { 
	N = (1<<20);
	FILE *f1 = fopen("in.txt", "w");
	FILE *f2 = fopen("h.txt", "w");
	complex *in_sig = (complex *)malloc(sizeof(complex)*N);
	complex *h_sig = (complex *)malloc(sizeof(complex)*N);
	complex *out_h = (complex *)malloc(sizeof(complex)*N);
	complex *out_fft = (complex *)malloc(sizeof(complex)*N);
	complex *out_conv = (complex *)malloc(sizeof(complex)*N);
	printf("Reading data... ");
	double tmp;
	for (int i = 0; i < N; i++) {
		fscanf(f1, "%lf", &tmp);
		in_sig[i] = tmp;
	}
	for (int i = 0; i < N; i++) {
		fscanf(f2, "%lf", &tmp);
		h_sig[i] = tmp;
	}
	printf("DONE\n");
	printf("Running FFT/IFFT routines... ");
	clock_t fft_begin = clock();
	out_fft = myfft(N, in_sig);
	out_h = myfft(N, h_sig);
	for (int i = 0; i < N; i++) out_fft[i] *= out_h[i];
	out_fft = myifft(N, out_fft);
	clock_t fft_end = clock();
	printf(" DONE in %lf ms\n", 1000*(double)(fft_end - fft_begin)/CLOCKS_PER_SEC);
	printf("Running convolution routines... ");
	clock_t conv_begin = clock();
	out_conv = convolve(in_sig, in_sig, 2*N - 1);
	clock_t conv_end = clock();
	printf(" DONE in %lf ms\n", 1000*(double)(conv_end - conv_begin)/CLOCKS_PER_SEC);
	free(in_sig);
	fclose(f1); fclose(f2);
	return 0;
}
