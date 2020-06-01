import numpy as np

a = np.array([[0.2, 0, 0, 0], [0.4, 0, 0, 4], [0.6, 0, 4, 0], [0.8, 4, 0, 0], [0.5, 1, 1, 1]])

def count(a):
    max_1 = 0
    max_2 = 0
    max_3 = 0
    min_1 = 0
    min_2 = 0
    min_3 = 0
    A = a[0]
    B = a[0]
    C = a[0]
    D = a[0]
    E = a[0]
    F = a[0]
    for i in range(len(a)):
        if a[i, 1] > max_1:
            D = a[i]
            max_1 = a[i, 1]
        if a[i, 2] > max_2:
            C = a[i]
            max_2 = a[i, 2]
        if a[i, 3] > max_3:
            E = a[i]
            max_3 = a[i, 3]
        if a[i, 1] < min_1:
            B = a[i]
            min_1 = a[i, 1]
        if a[i, 2] > min_2:
            A = a[i]
            min_2 = a[i, 2]
        if a[i, 3] > min_3:
            F = a[i]
            min_3 = a[i, 3]
    x_1, y_1, z_1, d_1 = coord(C, D, E)
    for point in a:
        if point[1]*x_1+point[2]*y_1+point[3]*z_1+d_1 == 0:
            print(point)



def coord(x, y, z):
    M = np.array(
        [[-x[1], y[1]-x[1], z[1]-x[1]],
        [-x[2], y[2]-x[2], z[2]-x[2]],
        [-x[3], y[3]-x[3], z[3]-x[3]]]
    )
    det = int(round(np.linalg.det(M)))
    det_x = int(round(np.linalg.det(M[1:, 1:])))
    det_y = int(round(-np.linalg.det(M[0::2, 1::1])))
    det_z = int(round(np.linalg.det(M[1::1, 1::1])))
    #print(det_x, det_y, det_z, det)
    return det_x, det_y, det_z, det


count(a)


