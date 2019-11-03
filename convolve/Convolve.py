import cv2 
import numpy as np
from matplotlib import pyplot as plt

def convolve3(image, mask):
    row, col = image.shape
    res = np.zeros((row, col), dtype=np.uint8)
    for x in range(1, row-1):
        for y in range(1, col-1):
            res[x][y] = mask[0][0]*img[x-1][y-1] + mask[0][1]*img[x-1][y] +                         mask[0][2]*img[x-1][y+1] + mask[1][0]*img[x][y-1] +                         mask[1][1]*img[x][y] + mask[1][2]*img[x][y+1] +                         mask[2][0]*img[x+1][y-1] + mask[2][1]*img[x+1][y] +                         mask[2][2]*img[x+1][y+1]
            
    return res

def convolve2(image, mask):
    row, col = image.shape
    res = np.zeros((row, col), dtype=np.uint8)
    for x in range(0, row-1):
        for y in range(0, col-1):
            res[x][y] = mask[0][0]*img[x][y] + mask[0][1]*img[x][y+1] +                         mask[1][0]*img[x+1][y] + mask[1][1]*img[x+1][y+1]
            
    return res

img = cv2.imread('wirebond_mask.tif', 0)

mask1 = np.array([[1,1,1], [1,1,1], [1,1,1]], np.int32)
res1 = convolve3(img, mask1)
res1 = res1//9

mask2_hor = np.array([[-1,0,1], [-2,0,2], [-1,0,1]], np.int32)
mask2_ver = np.array([[1,2,1], [0,0,0], [-1,-2,-1]], np.int32)
res2_x = convolve3(img, mask2_hor)
res2_y = convolve3(img, mask2_ver)

mask3_hor = np.array([[-1,0,1], [-1,0,1], [-1,0,1]], np.int32)
mask3_ver = np.array([[1,1,1], [0,0,0], [-1,-1,-1]], np.int32)
res3_x = convolve3(img, mask3_hor)
res3_y = convolve3(img, mask3_ver)

mask4_hor = np.array([[1,0], [0,-1]], np.int32)
mask4_ver = np.array([[0,1], [-1,0]], np.int32)
res4_x = convolve2(img, mask4_hor)
res4_y = convolve2(img, mask4_ver)

fig0, axs0 = plt.subplots(1, 3, figsize=(15, 10))
axs0[0].imshow(res1, cmap='gray')
axs0[0].set_title("Mean filter")
axs0[1].imshow(res2_x, cmap='gray')
axs0[1].set_title("Sobel filter X")
axs0[2].imshow(res2_y, cmap='gray')
axs0[2].set_title("Sobel filter Y")

fig1, axs1 = plt.subplots(1, 4, figsize=(15, 15))
axs1[0].imshow(res3_x, cmap='gray')
axs1[0].set_title("Prewitt filter X")
axs1[1].imshow(res3_y, cmap='gray')
axs1[1].set_title("Prewitt filter Y")
axs1[2].imshow(res4_x, cmap='gray')
axs1[2].set_title("2x2 Gradient filter X")
axs1[3].imshow(res4_y, cmap='gray')
axs1[3].set_title("2x2 Gradient filter Y")

plt.show()

