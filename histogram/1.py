import cv2
import numpy as np
import math
import copy

img     	= cv2.imread("gray1.jpg",0)
neg     	= copy.deepcopy(img)
log			= copy.deepcopy(img)
power		= copy.deepcopy(img)
equalize    = copy.deepcopy(img)


equalize    = cv2.equalizeHist(equalize)


(height, width) = img.shape
cv2.imshow('image', img) 

for i in range(width):
	for j in range(height):
		neg[i][j]	= 255-neg[i][j]
		log[i][j]	= 105*math.log(1 + (img[i][j]),10)
		power[i][j]	= 1*img[i][j]**0.7

cv2.imshow('negative', neg) 
cv2.imshow('log', log) 
cv2.imshow('power', power) 
cv2.imshow("equalize",equalize)
cv2.waitKey(0) 
cv2.destroyAllWindows() 