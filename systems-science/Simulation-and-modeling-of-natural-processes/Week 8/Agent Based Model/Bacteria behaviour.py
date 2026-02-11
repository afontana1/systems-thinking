"""Agent-based chemotaxis simulation for bacteria.

Algorithm:
- Each bacterium tracks its last sensed nutrient density.
- If density improves, continue forward with probability P1.
- If density worsens, continue forward with probability P2.
- Otherwise, randomize direction. Movement wraps around the domain.
"""
from __future__ import annotations

from dataclasses import dataclass
import math
import random
from typing import Iterable

import numpy as np
import matplotlib.pyplot as plt


@dataclass
class ChemotaxisField:
    """Radial nutrient field with higher density at the center."""

    size: float

    def density(self, x: float, y: float) -> float:
        return 1.0 / (1.0 + math.hypot(x - self.size / 2.0, y - self.size / 2.0))


@dataclass
class Bacterium:
    x: float
    y: float
    speed: float
    direction: float
    last_density: float

    @classmethod
    def spawn(cls, field: ChemotaxisField, speed: float, rng: random.Random) -> "Bacterium":
        x = rng.random() * field.size
        y = rng.random() * field.size
        direction = rng.random() * math.tau
        last_density = field.density(x, y)
        return cls(x=x, y=y, speed=speed, direction=direction, last_density=last_density)

    def step(self, field: ChemotaxisField, dt: float, p_high: float, p_low: float, rng: random.Random) -> None:
        current_density = field.density(self.x, self.y)
        if current_density > self.last_density:
            keep = rng.random() < p_high
        else:
            keep = rng.random() < p_low

        if not keep:
            self.direction = rng.random() * math.tau

        self.x = (self.x + dt * self.speed * math.cos(self.direction)) % field.size
        self.y = (self.y + dt * self.speed * math.sin(self.direction)) % field.size
        self.last_density = current_density


def render(field: ChemotaxisField, bacteria: Iterable[Bacterium], grid_size: int = 100) -> np.ndarray:
    """Render the nutrient field and bacteria positions to a grid."""

    m = np.zeros((grid_size, grid_size), dtype=float)
    for x in range(grid_size):
        for y in range(grid_size):
            fx = x * field.size / grid_size
            fy = y * field.size / grid_size
            m[y, x] = field.density(fx, fy)

    for b in bacteria:
        gx = int(b.x * grid_size / field.size)
        gy = int(b.y * grid_size / field.size)
        m[gy % grid_size, gx % grid_size] = 1.0
    return m


def main() -> None:
    rng = random.Random(1)

    speed = 2 * math.exp(-6)
    dt = 0.2
    size = 100 * math.exp(-6)
    p_high = 0.9
    p_low = 0.5
    n = 10

    field = ChemotaxisField(size=size)
    bacteria = [Bacterium.spawn(field, speed, rng) for _ in range(n)]

    plt.figure()
    plt.title("Bacteria chemotaxis")
    plt.ion()
    plt.show()

    for step in range(200):
        if step % 10 == 0:
            grid = render(field, bacteria)
            plt.imshow(grid, origin="lower")
            plt.gcf().canvas.draw()
            plt.pause(0.01)

        for b in bacteria:
            b.step(field, dt, p_high, p_low, rng)

    plt.ioff()
    plt.show()


if __name__ == "__main__":
    main()
