import numpy as np

def apply_fan(T, obstacle, vx=1.0):
    T_new = T.copy()
    nx, ny = T.shape

    for i in range(1, nx-1):
        for j in range(1, ny-1):

            if obstacle[i, j] == 1:
                continue

            # 🚀 Upwind scheme (stable advection)
            if vx > 0:
                adv = T[i, j] - T[i, j-1]
            else:
                adv = T[i, j+1] - T[i, j]

            T_new[i, j] -= vx * adv

    return T_new