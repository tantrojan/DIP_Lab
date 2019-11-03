import matplotlib.pyplot as mp
import cv2
import numpy as np 
	
img = cv2.imread('gray2.jpg',0) 

scale = int(input("Enter the scale:"))
height, width = img.shape
new_h = int(scale*height)
new_w = int(scale*width)

new_img = np.zeros(shape=(new_h,new_w))
new_img2 = np.zeros(shape=(height//2,width//2))


for i in range(new_h):
	for j in range(new_w):
		k = int(i/scale)
		l = int(j/scale)
		new_img[i][j] = img[k][l]

for i in range(height//2):
	for j in range(width//2):
		k = int(i*scale)
		l = int(j*scale)
		new_img2[i][j] = img[k][l]



mp.subplot(131),mp.imshow(img,cmap='gray')
mp.title('Original')
mp.subplot(132),mp.imshow(new_img,cmap='gray')
mp.title('Zoomed')
mp.subplot(133),mp.imshow(new_img2,cmap='gray')
mp.title('Shrinked')
mp.show()