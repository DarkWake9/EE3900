#include <stdio.h>
#include <math.h>


int main()
{
    int x[] = {1.0,2.0,3.0,4.0,2.0,1.0};
    int k = 20;
    int y[6];
    y[0] = x[0];
    y[1] = -0.5*y[0]+x[1];

    for (int n = 0; n<6; n++)
    {
        if (n < 6){
		    y[n] = -0.5*y[n-1]+x[n]+x[n-2];
        }
	    else if (n > 5 && n < 8) {
		    y[n] = -0.5*y[n-1]+x[n-2];
        }
	    else{
		    y[n] = -0.5*y[n-1];   
        }
    }

}