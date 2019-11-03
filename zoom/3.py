import cv2 
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('gray2.jpg',0)

row,col = img.shape

new = np.array(np.zeros((row,col)))
eight = np.array(np.zeros((row,col)))
seven = np.array(np.zeros((row,col)))
six = np.array(np.zeros((row,col)))
five = np.array(np.zeros((row,col)))

for x in range(row):
	for y in range(col):
		val=img[x][y]
		if val>=128:
			eight[x][y]=128
			val=val-128
		if val>=64:
			seven[x][y]=64
			val=val-64
		if val>=32:
			six[x][y]=32
			val=val-32
		if val>=16:
			five[x][y]=16
			val=val-16

new = img - eight - seven - six - five
print(new)

plt.subplot(121),plt.imshow(img,cmap='gray')
plt.title('Image'),plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(new,cmap='gray')
plt.title('Transformed Image'),plt.xticks([]),plt.yticks([])
plt.show()