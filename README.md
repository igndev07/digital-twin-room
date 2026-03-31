# 🔥 Digital Twin Thermal Flow Simulator


A 2D heat transfer simulation combining diffusion, advection, and obstacles, visualized in real-time with flow vectors.

---

## 🚀 Features

- Heat diffusion (Fourier heat equation)
- Advection (fan-driven flow using upwind scheme)
- Obstacle interaction (walls block heat flow)
- Real-time heatmap visualization
- Flow direction arrows
- Max temperature vs time graph

---

## 🧠 Core Physics

### Heat Diffusion

dT/dt = alpha * (d²T/dx² + d²T/dy²)

Discrete form:

T_new = T + alpha * (T_up + T_down + T_left + T_right - 4*T)

---

### Advection (Flow)

Upwind scheme:

T_new = T - vx * (T[i,j] - T[i,j-1])

---

### Combined Equation

Advection + Diffusion:

dT/dt + v · ∇T = alpha ∇²T

---

### Obstacles

- Represented as grid mask
- No heat flow through walls
- Velocity set to zero inside obstacles

---

## 🏗️ Project Structure

```
simulation/
  engine.py
  physics.py
  boundary.py
  sources.py

visualization/
  plot.py

main.py
config.py
```

---

## ⚙️ Parameters

- alpha → diffusion strength  
- vx → flow velocity  
- Q → heat source intensity  

---

## ▶️ Run

```
python main.py
```

---

## 📊 Output

- Heatmap simulation  
- Flow arrows  
- Temperature evolution graph  

---

## 🧠 Learnings

- Finite Difference Method (FDM)  
- Advection vs diffusion balance  
- Numerical stability (upwind scheme)  
- Basic CFD concepts  

---

## 🚀 Future Work

- Streamlines instead of arrows  
- Interactive controls  
- Multiple fans  
- 3D simulation  


