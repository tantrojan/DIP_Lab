import cv2 
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('gray1.jpg',0)

row,col = img.shape
new = np.array(np.zeros((row,col)))

for x in range(row):
	for y in range(col):
		val=(img[x][y])//32
		new[x][y]=((val)*8+4)*(8-val)

plt.subplot(121),plt.imshow(img,cmap='gray')
plt.title('Image'),plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(new,cmap='gray')
plt.title('Transformed Image'),plt.xticks([]),plt.yticks([])
plt.show()