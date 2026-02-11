# Week 3 - Lotka-Volterra Model

**Overview**
- Simulates predator-prey dynamics using the Lotka-Volterra equations with an explicit Euler integrator.

**Files**
- `Lotka_Volterra_model.py`: Model parameters, Euler integration, and plotting.

**Algorithm**
- Define derivatives for prey and predator populations.
- Step forward with explicit Euler: `y_{t+1} = y_t + dt * f(y_t)`.
- Visualize time series on log-log axes.

**Run**
```bash
python "Lotka_Volterra_model.py"
```

**Dependencies**
- `numpy`
- `matplotlib`
