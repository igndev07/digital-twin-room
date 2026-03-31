from simulation.engine import HeatSimulator , add_obstacle
from simulation.sources import add_sources
from simulation.boundary import apply_cooling
from visualization.plot import animate


sim = HeatSimulator(50, 50, alpha=0.02)

add_sources(sim)
add_obstacle(sim, 10, 20, 15, 35)  

animate(sim, apply_cooling)
