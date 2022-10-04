import numpy as np
import cv2
import scipy

def cross_corr(H, F):
    Hs = H.shape
    Fs = F.shape
    print(H)
    print(F)
    print(Hs)
    print(Fs)
    result = H.copy()[0:Hs[0] - Fs[0] + 1, 0:Hs[1] - Fs[1] + 1]
    for id1 in range(H.shape[0] - F.shape[0] + 1 ):
        for id2 in range(H.shape[1] - F.shape[1] + 1):
            result[id1][id2] = (F * H[id1 : id1 + Fs[0],id2 : id2 + Fs[1]]).sum() / (Fs[0] * Fs[1] * 2)
    return result

origin = cv2.imread("image/original.jpeg", cv2.IMREAD_GRAYSCALE)
filter = cv2.imread("image/filter.png", cv2.IMREAD_GRAYSCALE)

def min_max_normalize(x):
    Min = x.min()
    Max = x.max()
    return (x-Min)/(Max - Min)

def maxima(x):
    y = x.copy()
    Max = y.max()
    for id1 in range(y.shape[0]):
        for id2 in range(y.shape[1]):
            if (y[id1][id2] >= Max * 53 / 100):
                y[id1][id2] = 1
            else:
                y[id1][id2] = 0
    return y

origin = min_max_normalize(origin)
filter = min_max_normalize(filter)

print(origin)
print(filter)

cross_matrix1 = cross_corr(origin, filter)
cross_matrix2 = maxima(cross_matrix1)

cv2.imshow('origin', origin)
cv2.imshow('filter', filter)
cv2.imshow("result1", cross_matrix1)
cv2.imshow("result2", cross_matrix2)
cv2.waitKey(0)
