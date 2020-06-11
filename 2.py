import numpy as np
import itertools
from itertools import combinations


def coord(x, y, z):
    M = np.array(
        [[-x[1], y[1]-x[1], z[1]-x[1]],
        [-x[2], y[2]-x[2], z[2]-x[2]],
        [-x[3], y[3]-x[3], z[3]-x[3]]]
    )
    det = int(round(np.linalg.det(M)))
    det_x = int(round(np.linalg.det(M[1:, 1:])))
    det_y = int(round(-np.linalg.det(M[0::2, 1::1])))
    det_z = int(round(np.linalg.det(M[0:2:1, 1::1])))
    return det_x, det_y, det_z, det

#print(coord((0.2, 0, 0, 0), (0.4, 0, 0, 4), (0.6, 0, 4, 0)))

a = ([(0.7, 0, 0, 0), (1, 0, 1, 0), (1, 1, 0, 0), (1, 0, 0, 1)])


def g_point(a):
    comb = combinations(a, 3)
    gr_points = set ()
    for elem in comb:
        # print(elem)
        A, B, C, D = coord (elem[0], elem[1], elem[2])
        plus = 0
        minus = 0
        first = False
        granich = True
        for point in a:
            zn = A * point[1] + B * point[2] + C * point[3] + D
            # print(point,'   ', zn)
            if zn > 0 and first == False:
                plus = 1
                first = True
            if zn < 0 and first == False:
                minus = 1
                first = True

            if first and zn > 0 and minus == 1:
                granich = False
                break
            if first and zn < 0 and plus == 1:
                granich = False
                break
        if granich == True:
            for p in elem:
                gr_points.add (tuple (p))
    return len(gr_points)


mo = 0
for i in range(1, len(a)+1):
    com = combinations(a, i)
    for c in com:
        print(c)
        prob=1
        for point in a:
            if point in c:
                prob = prob*point[0]
            else:
                prob = prob*(1-point[0])
        if len(c) in [1, 2,3,4]:
            X = len(c)
        else:
            X = g_point(c)
        mo += X*prob
print(mo)

