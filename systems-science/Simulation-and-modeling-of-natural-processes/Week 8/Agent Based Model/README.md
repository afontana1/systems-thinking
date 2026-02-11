# Week 8 - Agent Based Model (Bacteria Chemotaxis)

**Overview**
- Simulates bacteria moving in a radial nutrient field using probabilistic persistence.

**Files**
- `Bacteria behaviour.py`: Bacteria agents, chemotaxis field, and visualization.
- `Bacteria.ipynb`: Notebook wrapper.

**Algorithm**
- Each bacterium compares current density to its previous density.
- Continue forward with probability `P1` if improved, `P2` otherwise.
- If not continuing, randomize direction and move with wrap-around.

**Run**
```bash
python "Bacteria behaviour.py"
```

**Dependencies**
- `numpy`
- `matplotlib`
