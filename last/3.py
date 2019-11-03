import cv2
import numpy as np

from scipy import ndimage
from math import sqrt

def magnitude(img1,img2,t):
    newimage=img1[:]
    for i in range(img1.shape[0]):
        for j in range(img1.shape[1]):
            newimage[i][j]=sqrt((img1[i][j]**2+img2[i][j]**2))
            if newimage[i][j]<t:
                newimage[i][j]=0
            else:
                newimage[i][j]=255

    return newimage


image =cv2.imread("house.jpeg",0)
# print(image)
avg=np.array([[1,1,1],
     [1, 1, 1],
     [1, 1, 1]])
# avg=np.array(avg)

img1=ndimage.convolve(image,avg , mode="constant", cval=0)
img1=img1/9
cv2.imshow("avg",img1)
vertical_kernel=np.array([[-1,0,1],
                            [-2,0,2],
                            [-1,0,1]])
horizontal_kernel=np.array([[-1,-2,-1],
                         [0,0,0],
                         [1,2,1]])


img1=ndimage.convolve(img1, vertical_kernel, mode="constant", cval=0)
img2=ndimage.convolve(img1, horizontal_kernel, mode="constant", cval=0)

img4=magnitude(img1,img2,50)
cv2.imshow("edges",img4)
cv2.waitKey(0)
cv2.destroyAllWindows()