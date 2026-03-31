import numpy as np

class HeatSimulator:
    def __init__(self, nx, ny, alpha):
        self.nx = nx
        self.ny = ny
        self.alpha = alpha
        self.T = np.ones((nx, ny)) * 25
        self.Q = np.zeros((nx, ny))
        self.obstacle = np.zeros((nx, ny))

    def add_heat_source(self, x, y, strength):
        self.Q[x, y] = strength

    def step(self):
        T_new = self.T.copy()

        for i in range(1, self.nx-1):
            for j in range(1, self.ny-1):
                if self.obstacle[i, j] == 1:
                    T_new[i, j] = 25  # ambient temp
                    continue

                flux = (
                self.T[i+1, j] + self.T[i-1, j] +
                self.T[i, j+1] + self.T[i, j-1] -
                4*self.T[i, j]
            )


                T_new[i, j] = self.T[i, j] + self.alpha * flux + 0.5*self.Q[i, j]
                

        self.T = T_new
        return self.T
    


def add_obstacle(sim, x1, x2, y1, y2):
    sim.obstacle[x1:x2, y1:y2] = 1