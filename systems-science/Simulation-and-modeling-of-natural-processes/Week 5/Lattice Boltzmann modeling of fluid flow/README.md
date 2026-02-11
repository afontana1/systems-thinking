# Week 5 - Lattice Boltzmann (D2Q9)

**Overview**
- Simulates 2D fluid flow on a lattice with a cylindrical obstacle using the D2Q9 LBM model.

**Files**
- `Lattice Boltzmann.py`: LBM simulator with collision, streaming, and bounce-back boundaries.
- `Lattice Boltzman.ipynb`: Notebook wrapper.

**Algorithm**
- Initialize distributions from equilibrium.
- Iterate: compute macroscopic fields, collide toward equilibrium, stream to neighbors.
- Apply bounce-back for the obstacle boundary.

**Run**
```bash
python "Lattice Boltzmann.py"
```

**Dependencies**
- `numpy`
- `matplotlib`
