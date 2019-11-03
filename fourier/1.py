'''Write a Program to obtain one-dimensional discrete Fourier transform of a
given one-dimensional vector consists of integer numbers generated randomly.
'''

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

print("\nTransformed list: ")
transformed_ls = []
for u in range(size):
    real, imag = 0, 0
    for x in range(size):
        A = random_ls[x]
        angle = 2 * math.pi*u*x/size
        real += A * math.cos(angle)
        imag += A * math.sin(angle)
    transformed_ls.append("({0:8.2f}) + ({0:8.2f})i".format(real,imag))
    print(transformed_ls[u])