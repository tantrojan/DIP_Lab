import cv2
import numpy as np

img = cv2.imread('house.jpeg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, bw_img = cv2. threshold(gray,127,255,cv2. THRESH_BINARY)
edges = cv2.Canny(bw_img,50,150,apertureSize = 3)

lines = cv2.HoughLines(edges,1,np.pi/180,200)
for rho,theta in lines[0]:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))

    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

plt.imshow(img)
plt.title('HoughLines')
plt.show()
