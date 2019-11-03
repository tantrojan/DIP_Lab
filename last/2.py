import cv2 
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread("house.jpeg",0)

vertical_kernel = np.array([[-1,0,1],[-2,0,2],[-1,0,1]],np.int32)
horizontal_kernel = np.array([[-1,-2,-1],[0,0,0],[1,2,1]],np.int32)

v_img = cv2.filter2D(img,-1,vertical_kernel)
h_img = cv2.filter2D(img,-1,horizontal_kernel)

plt.subplot(121),plt.imshow(v_img,cmap='gray')
plt.title('Vertical Lines'),plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(h_img,cmap='gray')
plt.title('Horizontal Lines'),plt.xticks([]),plt.yticks([])
plt.show()
