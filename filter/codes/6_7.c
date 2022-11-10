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
	for (int i = 0; i < n; i++) for (int j = 0; j <= i; j++) a[i] += h[j]*x[i - j];
	return a;
}

complex *dft(complex *x, int n) { 
    complex *X = (complex *)calloc(n, sizeof(complex));
    for (int i = 0; i < n; i++) { 
        for (int j = 0; j < n; j++) { 
            X[i] += x[j]*cexp(-I*2*M_PI*i*j/n);
        }
    }
    return X;
}

complex *idft(complex *x, int n) { 
    complex *X = (complex *)calloc(n, sizeof(complex));
    for (int i = 0; i < n; i++) { 
        for (int j = 0; j < n; j++) { 
            X[i] += x[j]*cexp(I*2*M_PI*i*j/n);
        }
        X[i] /= n;
    }
    return X;
}

complex **dftmtx(int n) { 
    complex **mtx = (complex **)calloc(n, sizeof(complex *));
    for (int i = 0; i < n; i++) mtx[i] = (complex *)calloc(n, sizeof(complex));
    for (int i = 0; i < n; i++) { 
        for (int j = 0; j < n; j++) { 
            mtx[i][j] = cexp(I*2*M_PI*i*j/n);
        }
    }
    return mtx;
}

complex **invmtx(int n) { 
    complex **mtx = (complex **)calloc(n, sizeof(complex *));
    for (int i = 0; i < n; i++) mtx[i] = (complex *)calloc(n, sizeof(complex));
    for (int i = 0; i < n; i++) { 
        for (int j = 0; j < n; j++) { 
            mtx[i][j] = cexp(-I*2*M_PI*j*i/n)/(double)n;
        }
    }
    return mtx;
}

int main(int argc, char *argv[]) { 
	FILE *f1 = fopen("fft.txt", "w");
	FILE *f2 = fopen("ifft.txt", "w");
	FILE *f3 = fopen("conv.txt", "w");
	FILE *f4 = fopen("dft.txt", "w");
	FILE *f5 = fopen("dftmtx.txt", "w");
    for (int j = 0; j <= 20; j++) {
    	srand(time(0));
    	int n = 1 << j;
    	complex *a = (complex *)malloc(sizeof(complex)*n);
    	for (int i = 0; i < n; i++) a[i] = (double)random()/RAND_MAX;
    	// FFT Simulations
    	clock_t fft_begin = clock();
    	a = myfft(n, a);
    	clock_t fft_end = clock();
    	// End FFT simulation
    	// IFFT simulation
    	clock_t ifft_begin = clock();
    	a = myifft(n, a);
    	clock_t ifft_end = clock();
    	// End IFFT simulation
    	fprintf(f1, "%lf\n", 1000*(double)(fft_end - fft_begin)/CLOCKS_PER_SEC);
    	fprintf(f2, "%lf\n", 1000*(double)(ifft_end - ifft_begin)/CLOCKS_PER_SEC);
    	free(a);
    }
	for (int j = 10; j <= 1000; j+=10) {
		int n = j;
		complex *h = (complex *)malloc(sizeof(complex)*n);
		for (int i = 0; i < n; i++) h[i] = (double)random()/RAND_MAX;
		complex *x = (complex *)malloc(sizeof(complex)*n);
		complex *dx = (complex *)malloc(sizeof(complex)*n);
		complex *ix = (complex *)malloc(sizeof(complex)*n);
		for (int i = 0; i < n; i++) x[i] = (double)random()/RAND_MAX, dx[i] = 0.0, ix[i] = 0.0;
	    // Convolution simulation
	    clock_t conv_begin = clock();
	    complex *y = convolve(h, x, n);
	    clock_t conv_end = clock();
	    // End convolution simulation
		fprintf(f3, "%lf\n", 1000*(double)(conv_end - conv_begin)/CLOCKS_PER_SEC);
        complex *Y = (complex *)malloc(sizeof(complex)*n);
        // DFT-IDFT simulation
        clock_t dft_begin = clock();
        complex *X = dft(x, n);
        complex *H = dft(h, n);
        for (int i = 0; i < n; i++) Y[i] = H[i]*X[i];
        y = idft(Y, n);
        clock_t dft_end = clock();
        // End DFT-IDFT simulation
		fprintf(f4, "%lf\n", 1000*(double)(dft_end - dft_begin)/CLOCKS_PER_SEC);
        // DFT Matrix simulation
        clock_t dftmtx_begin = clock();
        complex **dm = dftmtx(j);
        complex **idm = invmtx(j);
        for (int i = 0; i < n; i++) { 
            for (int j = 0; j < n; j++) { 
               dx[i] += dm[i][j]*x[j];
            }
        }
        for (int i = 0; i < n; i++) { 
            for (int j = 0; j < n; j++) { 
               ix[i] += idm[i][j]*dx[j];
            }
        }
        clock_t dftmtx_end = clock();
        // End DFT Matrix simulation
		fprintf(f5, "%lf\n", 1000*(double)(dftmtx_end - dftmtx_begin)/CLOCKS_PER_SEC);
        // Free allocated memory
        for (int i = 0; i < n; i++) { free(dm[i]); free(idm[i]); }
		free(x); free(h); free(y); free(dm); free(idm); free(dx); free(ix); free(X); free(H); free(Y); 
	}
	fclose(f1); fclose(f2); fclose(f3); fclose(f4); fclose(f5);
	// FFT-IFFT Tests
	int N = 8;
	complex* test = (complex *)malloc(sizeof(complex)*N);
	for (int i = 0; i < N; i++) test[i] = (double)random()/RAND_MAX;
	complex* fft_test = myfft(N, test);
	complex* ifft_test = myifft(N, fft_test);
	bool fl = true;
	for (int i = 0; i < N; i++) { 
		if (cabs(test[i] - ifft_test[i]) >= EPS) { 
			fl = false;
			break;
		}
	}
	printf("Testing FFT-IFFT combination... ");
	if (fl) printf("[OK]\n");
	else printf("[BAD]\n");
	for (int i = 0; i < N; i++) fft_test[i] = conj(fft_test[i]);
	ifft_test = myfft(N, fft_test);
	for (int i = 0; i < N; i++) ifft_test[i] = conj(ifft_test[i])/(1.0*N);
	fl = true;
	for (int i = 0; i < N; i++) { 
		if (cabs(test[i] - ifft_test[i]) >= EPS) { 
			fl = false;
			break;
		}
	}
	printf("Testing FFT algorithm... ");
	if (fl) printf("[OK]\n");
	else printf("[BAD]\n");
	free(test);
	// End Tests
	// Run Python Codes
	system("python 6_7_1.py");
	system("python 6_7_2.py");
	return 0;
}
