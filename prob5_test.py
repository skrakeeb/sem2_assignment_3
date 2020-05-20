'''
coded by: rakeeb
coded for: base code for prob5
'''
import numpy as np 
import matplotlib.pyplot as plt 
import time

d=1
x = np.arange(0,100+d,d)
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
time_1 = end1 - start	
time_2 = end2 - end1
print('time for my code:',time_1,'\ntime for numpy code:', time_2)