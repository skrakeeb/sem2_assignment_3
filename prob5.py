'''
coded by: rakeeb
coded for: comparing time taken for hand written code and np.fft.fft function for computing Fourier Tranceforms
'''

import numpy as np 
import matplotlib.pyplot as plt 
import time

selected_numbers = np.arange(4,104,4)  # numbers at which we will obtain DFT
time_array1 = np.zeros(selected_numbers.size)  # for hand written code
time_array2 = np.zeros(selected_numbers.size)  # for numpy code fft.fft


for r in range(selected_numbers.size):
	d=1
	x = np.arange(0,(selected_numbers[r])+d,d)
	k = np.zeros(x.size)
	f_t = np.zeros(x.size, dtype=np.complex_)
	start = time.time()
	for i in range(x.size):
		k[i] = 2*np.pi*i/(x.size*d)
		s = 0
		for j in range(x.size):
			factor = x[j]*np.exp(-1j *k[i]*x[j])
			s = s + factor

		f_t[i] = s*1/np.sqrt(x.size)  #fourier transform
	#print('FT by hand: \n',f_t)
	end1 = time.time()	
	fnew = np.fft.fft(x,norm= 'ortho')  #fourier  transform by numpy fft.fft
	#print('FT by numpy: \n',fnew)	
	end2 = time.time()
	time_array1[r] = end1 - start  # time array for my code	
	time_array2[r] = end2 - end1   # time array for numpy fft.fft

#print('time taken by code: ', time_array1,'\ntime taken by fft.fft: ',time_array2)

plt.plot(selected_numbers,time_array1,label='For my code')
plt.plot(selected_numbers,time_array2,label='For fft.fft')
plt.legend()
plt.xlabel('Selected numbers')
plt.ylabel('Time taken')
plt.grid()
plt.title('Comparison of time taken')
plt.show()
