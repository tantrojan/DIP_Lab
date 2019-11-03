from  math import e,pi
import copy,cv2

PI=pi

twodinput=cv2.imread("img1.jpg",0)
twodinput=cv2.resize(twodinput,(50,50))

M=len(twodinput)
N=len(twodinput[0])

x,y=0,0

twodftransform=[]
for i in range(M):
    twodftransform.append([])
    for j in range(N):
        twodftransform[-1].append(0)

for x in range(M):
    for y in range(N):
        sum=0
        m,n=0,0
        for m in range(M):
            for n in range(N):
                sum+=twodinput[m][n]*e**(-2j*pi*(((m*x)/M)+((n*y)/N)))

        twodftransform[x][y]=sum/(M*N)
    print(x)

realtf=twodinput[:]
for i in range(M):
    for j in range(N):
        realtf[i][j]=twodftransform[i][j].real


inversetf=copy.deepcopy(twodinput)
for x in range(M):
    for y in range(N):
        sum=0
        m,n=0,0
        for m in range(M):
            for n in range(N):
                sum+=realtf[m][n]*e**(2j*pi*(((m*x)/M)+((n*y)/N)))

        inversetf[x][y]=sum.real

cv2.imshow("input",twodinput)
cv2.imshow("fourier",realtf)
cv2.imshow("ff",inversetf)
cv2.waitKey(0)
cv2.destroyAllWindows()


