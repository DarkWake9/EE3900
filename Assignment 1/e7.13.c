#define _FFT_H

#include <stdio.h>

typedef unsigned int uint16u;
typedef unsigned char uint8;
typedef unsigned long uint32;
typedef int sint16;
typedef char sint8;
typedef long sint32;
typedef float fp32;
typedef double fp64;

#define FFT_N (8)//8-point FFT                  

typedef struct Complex
{
	fp32 re;
	fp32 im;
} complex;//A node unit in the complex FFT

//statement
complex WN0;
complex WN1;
complex WN2;
complex WN3;

complex ComplexMul(complex c1, complex c2);
complex ComplexAdd(complex c1, complex c2);
complex ReverseComplex(complex c);
void fft(complex *x, complex *r);
static void BitReverse(complex *x, complex *r, int n, int l);


complex WN0 = {1,0};  
complex WN1 = {0.7109, -0.7109};
complex WN2 = {0,-1};
complex WN3 = {-0.7109,-0.7109};

complex ComplexMul(complex c1, complex c2)
{
	complex r;

	r.re = c1.re*c2.re-c1.im*c2.im;//Re
	r.im = c1.re*c2.im + c1.im*c2.re;//Im

	return r;
}

complex ComplexAdd(complex c1, complex c2)
{
	complex r;

	r.re = c1.re + c2.re;
	r.im = c1.im + c2.im;

	return r;
}

complex ReverseComplex(complex c)
{
	c.re = -c.re;
	c.im = -c.im;

	return c;
}

/*
 * 8 point base-2 time FFT algorithm
 */
void fft(complex *x, complex *r)
{
	complex temp1[8];
	complex temp2[8];

	temp1[0] = x[0];
	temp1[1] = ComplexMul(x[1], WN0);
	temp1[2] = temp1[2] = x[2];
	temp1[3] = ComplexMul(x[3], WN0);
	temp1[4] = x[4];
	temp1[5] = ComplexMul(x[5], WN0);
	temp1[6] = x[6];
	temp1[7] = ComplexMul(x[7], WN0);

	temp2[0] = ComplexAdd(temp1[0],temp1[1]);
	temp2[1] = ComplexAdd(temp1[0],ReverseComplex(temp1[1]));
	temp2[2] = ComplexAdd(temp1[2],temp1[3]);
	temp2[3] = ComplexAdd(temp1[2],ReverseComplex(temp1[3]));
	temp2[4] = ComplexAdd(temp1[4],temp1[5]);
	temp2[5] = ComplexAdd(temp1[4],ReverseComplex(temp1[5]));
	temp2[6] = ComplexAdd(temp1[6],temp1[7]);
	temp2[7] = ComplexAdd(temp1[6],ReverseComplex(temp1[7]));

	temp2[2] = ComplexMul(temp2[2], WN0);
	temp2[3] = ComplexMul(temp2[3], WN2);
	temp2[6] = ComplexMul(temp2[6], WN0);
	temp2[7] = ComplexMul(temp2[7], WN2);

	temp1[0] = ComplexAdd(temp2[0],temp2[2]);
	temp1[1] = ComplexAdd(temp2[1],temp2[3]);
	temp1[2] = ComplexAdd(temp2[0],ReverseComplex(temp2[2]));
	temp1[3] = ComplexAdd(temp2[1],ReverseComplex(temp2[3]));
	temp1[4] = ComplexAdd(temp2[4],temp2[6]);
	temp1[5] = ComplexAdd(temp2[5],temp2[7]);
	temp1[6] = ComplexAdd(temp2[4],ReverseComplex(temp2[6]));
	temp1[7] = ComplexAdd(temp2[5],ReverseComplex(temp2[7]));

	temp1[4] = ComplexMul(temp1[4], WN0);
	temp1[5] = ComplexMul(temp1[5], WN1);
	temp1[6] = ComplexMul(temp1[6], WN2);
	temp1[7] = ComplexMul(temp1[7], WN3);

	r[0] = ComplexAdd(temp1[0], temp1[4]);
	r[1] = ComplexAdd(temp1[1], temp1[5]);
	r[2] = ComplexAdd(temp1[2], temp1[6]);
	r[3] = ComplexAdd(temp1[3], temp1[7]);
	r[4] = ComplexAdd(temp1[0], ReverseComplex(temp1[4]));
	r[5] = ComplexAdd(temp1[1], ReverseComplex(temp1[5]));
	r[6] = ComplexAdd(temp1[2], ReverseComplex(temp1[6]));
	r[7] = ComplexAdd(temp1[3], ReverseComplex(temp1[7]));
}

/*
 * Reverse order transformation
 */
static void BitReverse(complex *x, complex *r, int n, int l)
{
	int i = 0;
	int j = 0;
	short stk = 0;
	static complex *temp = 0;

	temp = (complex *)malloc(sizeof(complex) * n);
	if (!temp) {
		return;
	}

	for(i=0; i<n; i++) {
		stk = 0;
		j = 0;
		do {
			stk |= (i>>(j++)) & 0x01;
			if(j<l)
			{
				stk <<= 1;
			}
		}while(j<l);

		if(stk <n) {/* Satisfy the reverse order output */
			temp[stk] = x[i];
		}
	}
	/* copy @temp to @r */
	for (i=0; i<n; i++) {
		r[i] = temp[i];
	}
	free(temp);
}

int main(void)
{
	complex a[8] = { {1,0}, {2,0}, {3,0}, {4,0}, {2,0}, {1,0}, {0,0}, {0,0}};
	complex r[8];
	int i = 0;

	BitReverse(a, a, 8, 3);//Reverse order
	fft(a, r);
	for(i=0; i<8; i++)
	{
		printf("(%.4f) + j(%.4f)\n", r[i].re, r[i].im);
	}

	return 0;
}