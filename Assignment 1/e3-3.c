#include <stdio.h>
#include <math.h>


int main()
{
    FILE *fpx=NULL;
    FILE *fpy=NULL;
    fpx=fopen("x.dat","w");
    fpy=fopen("y.dat","w");

    double x[] = {1.0,2.0,3.0,4.0,2.0,1.0};
    int k = 20;
    double y[k];
    y[0] = x[0];
    y[1] = -0.5*y[0]+x[1];

    for (int n = 0; n < k; n++)
    {
        if (n < 6)
        {
		    y[n] = -0.5*y[n-1]+x[n]+x[n-2];
        }
	    else if (n > 5 && n < 8) 
        {
		    y[n] = -0.5*y[n-1]+x[n-2];
        }
	    else
        {
		    y[n] = -0.5*y[n-1];   
        }
    }
    for (int n = 0; n < 6; n++)
    {
        fprintf(fpx, "%lf\n", x[n]);
    }
    fclose(fpx);
    for (int n = 0; n < k; n++)
    {
        fprintf(fpy, "%lf\n", y[n]);
    }
    fclose(fpy);
    return 0;
}
