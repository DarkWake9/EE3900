#include <stdio.h>
#include <stdbool.h>
#include <math.h>
#include <stdlib.h>
#include <complex.h>
#include <time.h>
#define EPS 1e-6

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

int main() { 
	int n = 8;
	complex *a = (complex *)malloc(sizeof(complex)*n);
	a[0] = 1.0, a[1] = 2.0, a[2] = 3.0, a[3] = 4.0, a[4] = 2.0, a[5] = 1.0, a[6] = 0.0, a[7] = 0.0;
	a = myfft(n, a);
	for (int i = 0; i < n; i++) printf("X(%d) = %lf + %lfj\n", i, creal(a[i]), cimag(a[i]));
	free(a);
	return 0;
}
