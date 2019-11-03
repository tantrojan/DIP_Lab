import numpy as np
import cv2
from matplotlib import pyplot as plt


def find_nearest_above(my_array, target):
    diff = my_array - target
    mask = np.ma.less_equal(diff, -1)

    if np.all(mask):
        c = np.abs(diff).argmin()
        return c  
    masked_diff = np.ma.masked_array(diff, mask)
    return masked_diff.argmin()


def hist_match(original, specified):

    oldshape = original.shape
    original = original.ravel()
    specified = specified.ravel()

    s_values, bin_idx, s_counts = np.unique(
        original, return_inverse=True, return_counts=True)
    t_values, t_counts = np.unique(specified, return_counts=True)

    s_q = np.cumsum(s_counts).astype(np.float64)
    s_q /= s_q[-1]

    t_q = np.cumsum(t_counts).astype(np.float64)
    t_q /= t_q[-1]

    sour = np.around(s_q * 255)
    temp = np.around(t_q * 255)

    b = []
    for data in sour:
        b.append(find_nearest_above(temp, data))
    b = np.array(b, dtype='uint8')

    return b[bin_idx].reshape(oldshape)


def main():
    source = cv2.imread('ship1.jpg', 0)
    template = cv2.imread('boat1.jpg', 0)

    equalized = cv2.equalizeHist(source)
    matched = hist_match(source, template)

    plt.subplot(131),plt.imshow(source,cmap='gray')
    plt.title('Source')
    plt.subplot(132),plt.imshow(equalized,cmap='gray')
    plt.title('Equalized')
    plt.subplot(133),plt.imshow(matched,cmap='gray')
    plt.title('Matched')
    plt.show()


if __name__ == '__main__':
    main()
