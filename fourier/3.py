import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import random
import math

size = 15

random_ls = []
for i in range(size):
    random_ls.append(random.randint(0,256))
print("Input: ", end=" ")
print(random_ls)


transformed_ls = []
conjugate_ls = []
for u in range(size):
    real, imag, con_real, con_imag= 0, 0, 0, 0
    for x in range(size):
        A = random_ls[x]
        angle = 2 * math.pi*(u)*x/size
        con_angle = -angle
        real += A * math.cos(angle)
        imag += A * math.sin(angle)
        con_real += A * math.cos(con_angle)
        con_imag += A * math.sin(con_angle)
    conjugate_ls.append((con_real,-con_imag))
    transformed_ls.append((real,imag))

print("Fourier: ", end=" ")
print(transformed_ls)
print("Conjugate: ", end=" ")
print(conjugate_ls)