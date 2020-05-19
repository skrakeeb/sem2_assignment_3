import numpy as np 
import matplotlib.pyplot as plt 

def f(x):
	if x != 0:
		return(np.exp(-x**2))
	else:
		return(1)
		

x_min= -50
x_max= 50
n= 256   #number of points taken
dx= (x_max - x_min)/(n-1)
x= np.zeros(n)
y= np.zeros(n)

for i in range(n):
	x[i]= x_min + i*dx
	y[i]= f(x[i])

y_ft_np= np.fft.fft(y,norm='ortho') # Fourier transform that numpy gives

k_np= np.fft.fftfreq(n, d= dx)  # k values  that numpy returns
k=    2*np.pi*k_np              # true values of k

ph_factor= np.exp( -1j *k*x_min) #phase factor 
y_ft = dx * np.sqrt(n/(2.0*np.pi)) * ph_factor * y_ft_np # True Fourier transform 


plt.plot(x,y,'r')
plt.scatter(x,y)
plt.title('Plot of sinc function')
plt.show()	

plt.plot(k,y_ft,'b')
plt.scatter(k,y_ft)
plt.title('Plot of Fourier tansform')
plt.show()