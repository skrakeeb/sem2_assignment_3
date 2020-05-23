#plotting of the numerical data obatined by running prob4.c

import numpy as np
import matplotlib.pyplot as plt

#the analytical result
def f(x):
    return( np.exp(- np.sqrt(np.pi)*(np.pi**2)*(x**2) ))
     

k, ft_real, ft_img , ft_abs = np.loadtxt("prob4.txt", delimiter= ' ', unpack= True, skiprows= 1)

y_ft_analytic = np.zeros(k.size)

for i in range(k.size):
	y_ft_analytic[i] = f(k[i])

plt.plot(k, ft_abs ,'r', label= 'by FFTW')
plt.plot(k, y_ft_analytic, label= 'analytic')
plt.legend()
plt.show()