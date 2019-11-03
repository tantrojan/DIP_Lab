import cv2 
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('gray1.jpg',0)
img2 = cv2.imread('gray2.jpg',0)

shape = img.shape
new = np.array(np.zeros(shape))

for x in range(shape[0]):
	for y in range(shape[1]):
		new[x][y]=img[x][y]//2+img2[x][y]//2

plt.imshow(new,cmap='gray')
plt.title('Addition of two images'),plt.xticks([]),plt.yticks([])
plt.show()