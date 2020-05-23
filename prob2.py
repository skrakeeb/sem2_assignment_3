#plotting the numerical data obatined by running prob2.c

import numpy as np
import matplotlib.pyplot as plt

#the analytical result
def f(x):
    if(abs(x)<1.0):
        return(np.sqrt(np.pi/2.0))
    else:
        return(0.0)

k, ft_real, ft_img , ft_abs = np.loadtxt("prob2.txt", delimiter= ' ', unpack= True, skiprows= 1)

y_ft_analytic = np.zeros(k.size)

for i in range(k.size):
	y_ft_analytic[i] = f(k[i])

plt.plot(k, ft_abs ,'r',label= 'by FFTW')
plt.plot(k, y_ft_analytic,label= 'Analytic function')
plt.legend()
plt.xlabel('k')
plt.ylabel('function')
plt.title('Plot of Fourier transform')
plt.show()
