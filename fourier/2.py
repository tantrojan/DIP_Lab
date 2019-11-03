'''
Write a program to obtain two-dimensional discrete Fourier transform and its 
inverse of a gray level image of size 500*500. Also compute the magnitude, 
phase angle and power spectrum of the Fourier transform. 
'''

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('gray2.jpg', 0)

dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)

magnitude = cv2.magnitude(dft_shift[:,:,0], dft_shift[:,:,1])
phase_angle = cv2.phase(dft_shift[:,:,0], dft_shift[:,:,1])
power = magnitude**2

power_spectrum = 20*np.log(power)

inverse = np.fft.ifftshift(dft_shift)
img_back = cv2.idft(inverse)
img_back = cv2.magnitude(img_back[:,:,0],img_back[:,:,1])

fig, axs = plt.subplots(1, 3, figsize=(15, 15))

axs[0].imshow(img, cmap = 'gray')
axs[0].set_title('Input Image')
axs[1].imshow(power_spectrum, cmap = 'gray')
axs[1].set_title('Power Spectrum')
axs[2].imshow(img_back, cmap = 'gray')
axs[2].set_title('Inverse Fourier')

plt.show()