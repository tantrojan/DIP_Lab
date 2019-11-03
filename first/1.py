import cv2 
import numpy as np
from matplotlib import pyplot as plt

color = cv2.imread('img.jpg')
grayscale = cv2.imread('img.jpg',0)

bw = cv2.imread('img.jpg',0)
row,col = bw.shape

for x in range(row):
	for y in range(col):
		if bw[x][y]<126:
			bw[x][y]=0
		else:
			bw[x][y]=255

plt.subplot(131),plt.imshow(color)
plt.title('Color Image'),plt.xticks([]),plt.yticks([])
plt.subplot(132),plt.imshow(grayscale,cmap='gray')
plt.title('Grayscale Image'),plt.xticks([]),plt.yticks([])
plt.subplot(133),plt.imshow(bw,cmap='gray')
plt.title('Black and White'),plt.xticks([]),plt.yticks([])
plt.show()