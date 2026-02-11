# Week 6 - N-Body Simulation (Barnes-Hut)

**Overview**
- Approximates gravitational forces using a quadtree (Barnes-Hut) to reduce complexity.

**Files**
- `Barnes Hut Algorithm.py`: Quadtree, force calculation, and visualization.

**Algorithm**
- Build a quadtree with mass and center of mass per node.
- Approximate distant nodes as a single mass if `s / d < theta`.
- Integrate with a symplectic Euler step.

**Run**
```bash
python "Barnes Hut Algorithm.py"
```

**Dependencies**
- `numpy`
- `matplotlib`
