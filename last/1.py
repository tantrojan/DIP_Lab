import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('points.jpeg',0)
row,col = img.shape

laplacian=np.array([[-1,-1,-1],[-1, 8, -1],[-1, -1, -1]],np.int32)

new = np.zeros((row,col))
new = cv2.filter2D(img,-1,laplacian)

for x in range(row):
	for y in range(col):
		if new[x][y] < 5:
			new[x][y]=0
		else:
			new[x][y]=255
			
print(new)
plt.imshow(new, cmap='gray')
plt.title('Extracted Points')
plt.show()

