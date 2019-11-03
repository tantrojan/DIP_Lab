import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('gray1.jpg',0)
row, col = img.shape

gauss = np.random.normal(20,10,(row,col))
rayleigh = np.random.rayleigh(20,(row,col))
gamma = np.random.gamma(1, 20, (row,col)) 
exponential = np.random.exponential(10, (row,col))
uniform = np.random.uniform(2, 12, (row,col))


noisy = img + gauss
smooth_part = noisy[:100, :100]


plt.subplot(321),plt.hist(rayleigh.ravel(),256,[0,256])
plt.title('Rayleigh Distribution Image'), plt.xticks([]), plt.yticks([])
plt.subplot(322),plt.hist(gauss.ravel(),256,[0,256])
plt.title('Gauss Distribution'), plt.xticks([]), plt.yticks([])
plt.subplot(323),plt.imshow(img,cmap = 'gray')
plt.title('Input image'), plt.xticks([]), plt.yticks([])
plt.subplot(325),plt.hist(img.ravel(),256,[0,256])
plt.title('Input Image Histogram'), plt.xticks([]), plt.yticks([])
plt.subplot(324),plt.hist(noisy.ravel(),256,[0,256])
plt.title('Noisy Image Histogram'), plt.xticks([]), plt.yticks([])
plt.subplot(326),plt.hist(smooth_part.ravel(),256,[0,256])#; plt.show()
plt.title('Estimated Noise Distribution'), plt.xticks([]), plt.yticks([])
plt.show()
