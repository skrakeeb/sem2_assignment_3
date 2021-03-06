/* coded by: rakeeb
   coded for: Fourier transform of sinc function using FFTW3 library 
*/

#include <stdio.h>    
#include <stdlib.h>
#include <math.h>
#include <fftw3.h>
// run: gcc prob4.c -lfftw3 -lm
// out: ./a.out

// defining gaussian function
float f( float x)
{
	return exp(- pow(x,2));
}

void main()
{
	int numpoints = 256;
	float x_min= -50, x_max= 50, dx = (x_max-x_min)/(numpoints-1) , k ;
	float x_arr[numpoints], y_ft_absolute;
	fftw_complex y[numpoints], y_ft[numpoints];
	fftw_plan p;
	
	// sampling the function y = f(x)
	int i;
	for(i=0; i<numpoints; i++)
	{
		x_arr[i] = x_min + i*dx;
		y[i][0] = f(x_arr[i]); y[i][1]=0.0;  //making the y array           
	}	
    
    //computing fft using fftw
    p = fftw_plan_dft_1d(numpoints, y, y_ft, FFTW_FORWARD, FFTW_ESTIMATE);             	
	fftw_execute(p);


    //data storing 
    FILE *data2;
    data2 = fopen("prob4.txt","w");
    fprintf(data2, "# k, ft_real, ft_img, ft_absolute. delimeter = ' '\n");

	for(i=0; i<numpoints; i++)
	{
		if(i<=(numpoints/2-1))   //making the k values
		{
			k = 2*M_PI*i/(numpoints*dx);        
		}
		else
		{
			k = 2*M_PI*(i-numpoints)/(numpoints*dx);
	    }
        
        // actual values of DFT when x_min != 0
		y_ft[i][0] = dx*sqrt(1/(2*M_PI)) * (cos(k*x_min) * y_ft[i][0] + sin(k*x_min) * y_ft[i][1]);
	   	y_ft[i][1] = dx*sqrt(1/(2*M_PI)) * (cos(k*x_min) * y_ft[i][1] - sin(k*x_min) * y_ft[i][0]);

	    y_ft_absolute =  sqrt( pow(y_ft[i][0],2) + pow( y_ft[i][1],2) );  // absolute value of the Fourier transform

	    fprintf(data2, "%f %f %f %f\n", k, y_ft[i][0], y_ft[i][1], y_ft_absolute);
	}

	fclose(data2);

	fftw_destroy_plan(p);    


}
