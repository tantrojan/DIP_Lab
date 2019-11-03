'''Write a program to demonstrate the basics of filtering in the frequency domain.
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('peppers_gray.tif', 0)
dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)

rows, cols = img.shape
crow, ccol = rows//2, cols//2

# High pass filter
fshift = np.fft.fftshift(dft)
fshift[crow-30:crow+30, ccol-30:ccol+30] = [0, 0]
f_ishift = np.fft.ifftshift(fshift)
img_hpf = cv2.idft(f_ishift)
img_hpf = cv2.magnitude(img_hpf[:,:,0], img_hpf[:,:,1])

# Low pass Filter
mask = np.zeros((rows, cols, 2), np.uint8)
mask[crow-30:crow+30, ccol-30:ccol+30] = [1, 1]
fshift = np.fft.fftshift(dft) * mask
f_ishift = np.fft.ifftshift(fshift)
img_lpf = cv2.idft(f_ishift)
img_lpf = cv2.magnitude(img_lpf[:,:,0], img_lpf[:,:,1])

fig, axs = plt.subplots(1, 3, figsize=(15, 15))

axs[0].imshow(img, cmap = 'gray')
axs[0].set_title('Input Image')
axs[1].imshow(img_hpf, cmap = 'gray')
axs[1].set_title('High Pass Filter')
axs[2].imshow(img_lpf, cmap = 'gray')
axs[2].set_title('Low Pass Filter')

plt.show()