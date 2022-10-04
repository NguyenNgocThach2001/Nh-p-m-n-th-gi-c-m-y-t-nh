import numpy as np

def cross_corr(H, F):
    Hs = H.shape
    Fs = F.shape
    print(H)
    print(F)
    print(Hs)
    print(Fs)
    result = [[i for i in range(H.shape[0])] for j in range(H.shape[1])]
    for id1 in range(H.shape[0]):
        for id2 in range(H.shape[1]):
            sum = 0
            for id3 in range(F.shape[0]):
                for id4 in range(F.shape[1]):
                    i = id3 - F.shape[0] // 2
                    j = id4 - F.shape[1] // 2
                    if(id1 + i < 0 or id1 + i >= H.shape[0] or id2 + j < 0 or id2 + j >= H.shape[1]):
                        continue
                    sum += H[id1 + i][id2 + j] * F[id3][id4]
            result[id1][id2] = sum
    return result

H = np.ndarray((15,15)) 
F = np.empty((5,5)) 
H[:] = 1
F[:] = 1
cross_matrix = cross_corr(H, F)
print(cross_matrix)