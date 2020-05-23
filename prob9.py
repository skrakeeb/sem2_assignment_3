import numpy as np 
import matplotlib.pyplot as plt 
 

def f(x):
	if abs(x) < 1 :
		return(1)
	else :
		return(0)
x_min = -2
x_max = 2
num_points = 100
dx = (x_max - x_min)/(num_points-1)
x = np.arange(x_min,x_max + dx, dx)
y = np.zeros(x.size)

for i in range(x.size):
	y[i] = f(x[i])

ft_y = np.fft.fft(y, n= 2*num_points, norm= 'ortho')

k = np.fft.fftfreq(2*num_points, d= dx)
k = 2*np.pi*k                                 # true k values
dk = k[1] - k[0]

x_pad = np.fft.fftfreq(2*num_points, d= dk)   #padded x array
x_pad = 2*np.pi*x_pad                         #true x padded values

factor=np.exp(-1j* k* x_min)   # factor for taking account of x_min != 0
ex_ft_y = factor * ft_y        # exact Fourier transform

conv = dx * np.sqrt(2*num_points) * np.fft.ifft( ex_ft_y**2, norm = 'ortho')  # convolution with itself



plt.plot(k,ex_ft_y, 'r')
plt.title('Plot of Fourier transform')
plt.grid()
plt.xlabel('k')
plt.ylabel('DFT')
plt.show()

plt.plot(x, y, 'b', label= 'Given function')
plt.plot(x_pad, conv, 'r', label= 'Convolution')
plt.xlabel('x')
plt.ylabel('Functions')
plt.legend()
plt.show()


