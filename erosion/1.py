import numpy as np
import cv2
from matplotlib import pyplot as plt
import copy

def threshold(img):
	
	row,col = img.shape

	for x in range(row):
		for y in range(col):
			if img[x][y]<126:
				img[x][y]=0
			else:
				img[x][y]=255

	return img

def erosion(img):

	eroded = copy.deepcopy(img)
	row,col = eroded.shape

	movements = [[0,0],[0,1],[1,0],[1,1],[-1,-1],[-1,1],[1,-1],[0,-1],[-1,0]]
	for x in range(1,row-1):
		for y in range(1,col-1):
			flag=1

			for i in movements:
				if img[x+i[0]][y+i[1]]==0:
					flag=0
					break

			eroded[x][y]=255*flag

	return eroded

def dilation(img):

	dilated = copy.deepcopy(img)
	row,col = dilated.shape

	movements = [[0,0],[0,1],[1,0],[1,1],[-1,-1],[-1,1],[1,-1],[0,-1],[-1,0]]
	for x in range(1,row-1):
		for y in range(1,col-1):
			flag=0

			for i in movements:
				if img[x+i[0]][y+i[1]]==255:
					flag=1
					break

			dilated[x][y]=255*flag

	print(dilated)
	return dilated


img = cv2.imread('img3.jpg',0)
img = threshold(img)

eroded = erosion(img)
dilated = dilation(img)
opening = dilation(erosion(img))
closing = dilation(erosion(img))
bound = dilated-eroded

plt.subplot(231),plt.imshow(img,cmap='gray')
plt.title('Original'),plt.xticks([]),plt.yticks([])
plt.subplot(232),plt.imshow(eroded,cmap='gray')
plt.title('Erosion'),plt.xticks([]),plt.yticks([])
plt.subplot(233),plt.imshow(dilated,cmap='gray')
plt.title('Dilation'),plt.xticks([]),plt.yticks([])
plt.subplot(234),plt.imshow(bound,cmap='gray')
plt.title('Boundary'),plt.xticks([]),plt.yticks([])
plt.subplot(235),plt.imshow(opening,cmap='gray')
plt.title('Opening'),plt.xticks([]),plt.yticks([])
plt.subplot(236),plt.imshow(closing,cmap='gray')
plt.title('Closing'),plt.xticks([]),plt.yticks([])
plt.show()


