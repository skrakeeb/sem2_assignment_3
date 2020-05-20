'''
coded by: rakeeb
coded for: computing Fourier Tranceform of a 2d Gaussian
'''

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x_min = -10
x_max = 10
nx = 1000  # total point taken along x axis
dx = (x_max - x_min)/nx   # spacing along x

y_min = -10
y_max = 10
ny = nx
dy = (y_max - y_min)/ny  

x = np.arange(x_min, x_max+dx, dx)
y = np.arange(y_min, y_max+dy, dy)

k_x = np.fft.fftfreq(x.size, d=dx)   # k values for x
k_y = np.fft.fftfreq(y.size, d=dy)   # k values for y

# Creating grids:
xx ,yy = np.meshgrid(x,y, indexing='ij')    
k_xx, k_yy = np.meshgrid(k_x, k_y, indexing='ij')

f = np.exp(- (xx**2 + yy**2))  # given fn
ft_f = np.fft.fft2(f)         # 2d Fourier transform
#print(ft_f)

fig1 = plt.figure()
ax1 = Axes3D(fig1)
surf_plt1 = ax1.plot_surface(xx, yy, np.abs(f), cmap='Blues')
plt.title('Plot of the function')

fig2 = plt.figure()
ax2 = Axes3D(fig2)
surf_plt2 = ax2.plot_surface(k_xx, k_yy, np.abs(ft_f)*dx*dy, cmap='Reds')
plt.title('Plot of Fourier transform')

# Analytical soln:
ft_f_analytical = np.pi * np.exp(- (np.pi**2) * ( k_xx**2 + k_yy**2 ))
fig3 = plt.figure()
ax3 = Axes3D(fig3)
surf_plt3 = ax3.plot_surface(k_xx, k_yy, np.abs(ft_f_analytical), cmap='Greens')
plt.title('Plot of analytical Fourier transform')

plt.show()



