import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from simulation.physics import apply_fan
import numpy as np

def animate(sim, boundary_func):
    fig, ax = plt.subplots()
    display = sim.T.copy()
    display[sim.obstacle == 1] = 120  # force obstacle to max color

    T_plot = sim.T.copy()

    T_plot[sim.obstacle == 1] = -10  # something outside normal range

    cmap = plt.cm.hot.copy()
    cmap.set_under(color='#444444')  # wall color

    mat = ax.matshow(T_plot, cmap=cmap, vmin=20, vmax=120)
    plt.colorbar(mat)

    nx, ny = sim.T.shape
    X, Y = np.meshgrid(np.arange(ny), np.arange(nx))

    U = np.ones_like(sim.T) * 0.5   # x-direction flow
    V = np.zeros_like(sim.T)        # y-direction


    U[sim.obstacle == 1] = 0
    V[sim.obstacle == 1] = 0

    quiv = ax.quiver(X, Y, U, V, color='cyan', scale=20)

    temps = []

    def update(frame):
        # Step simulation
        sim.step()
        sim.T = apply_fan(sim.T, sim.obstacle, vx=0.3)
        sim.T = boundary_func(sim.T)

        # Store data for graph
        T_plot = sim.T.copy()
        T_plot[sim.obstacle == 1] = -10
        temps.append(sim.T.max())

        mat.set_array(T_plot)
        return [mat]

    ani = FuncAnimation(fig, update, frames=300, interval=50)

    plt.title("2D Thermal Flow Simulation (Advection + Diffusion + Obstacles)")
    plt.show()

    # 📈 Plot temperature graph AFTER simulation
    plt.figure()
    plt.plot(temps)
    plt.title("Max Temperature vs Time")
    plt.xlabel("Time Step")
    plt.ylabel("Temperature")
    plt.grid()
    plt.show()