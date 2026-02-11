# Week 4 - Cellular Automata (Langton's Ant)

**Overview**
- Implements Langton's Ant on a toroidal grid.

**Files**
- `Automata Ant.py`: Ant, grid, simulation loop, and visualization.
- `Ant_Movement.ipynb`: Notebook that runs the same simulation.

**Algorithm**
- On a white cell: turn right, flip to black.
- On a black cell: turn left, flip to white.
- Move forward one cell (wrap around edges).

**Run**
```bash
python "Automata Ant.py"
```

**Dependencies**
- `numpy`
- `matplotlib`
