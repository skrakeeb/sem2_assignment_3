import numpy as np 
import matplotlib.pyplot as plt 
from scipy import signal

y = np.loadtxt('noise.txt')
fs = 1e5  # sampling frequency
ts = 1/float(fs)  # time difference between two measurement
time = np.arange(0,y.size * ts, ts)


y_ft = np.fft.fft(y)
k_values = 2* np.pi * np.fft.fftfreq(y.size)

plt.plot(time,y)
plt.title('Plot of the noise')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.show()

plt.plot(k_values,y_ft,'r')
plt.title('Plot of Fourier transform')
plt.xlabel('k')
plt.ylabel('Funtional values')
plt.show()

f, Pyy_den = signal.periodogram(y, fs)   # f= sample frequency, Pyy_den = power spectral density 
plt.semilogy(f, Pyy_den)
plt.ylim([1e-8, 1e-3])
plt.xlabel('Frequency [Hz]')
plt.ylabel('Power Spectral Density')
plt.grid()
plt.show()