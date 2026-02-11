"""Langton's Ant cellular automaton.

Algorithm:
- The ant stands on a grid cell with a binary color (0/1).
- If on white (0), turn right, flip cell to 1.
- If on black (1), turn left, flip cell to 0.
- Move forward one cell (toroidal wrapping).
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

import numpy as np
import matplotlib.pyplot as plt


Direction = int  # 0=right, 1=down, 2=left, 3=up


@dataclass
class Grid:
    """Square grid for Langton's Ant."""

    size: int
    cells: np.ndarray

    @classmethod
    def empty(cls, size: int) -> "Grid":
        return cls(size=size, cells=np.zeros((size, size), dtype=np.uint8))

    def flip(self, x: int, y: int) -> None:
        self.cells[y, x] ^= 1

    def color(self, x: int, y: int) -> int:
        return int(self.cells[y, x])

    def wrap(self, x: int, y: int) -> tuple[int, int]:
        return x % self.size, y % self.size


@dataclass
class Ant:
    """Ant with position and direction."""

    x: int
    y: int
    direction: Direction

    def step(self, grid: Grid) -> None:
        color = grid.color(self.x, self.y)
        if color == 0:
            self.direction = (self.direction + 1) % 4  # right
        else:
            self.direction = (self.direction - 1) % 4  # left
        grid.flip(self.x, self.y)

        dx, dy = direction_vector(self.direction)
        self.x, self.y = grid.wrap(self.x + dx, self.y + dy)


def direction_vector(direction: Direction) -> tuple[int, int]:
    if direction == 0:
        return (1, 0)
    if direction == 1:
        return (0, 1)
    if direction == 2:
        return (-1, 0)
    return (0, -1)


def simulate(grid: Grid, ant: Ant, steps: int) -> Iterable[np.ndarray]:
    """Yield grid states as the ant moves."""

    for _ in range(steps):
        ant.step(grid)
        yield grid.cells


def visualize(grid: Grid, ant: Ant, steps: int) -> None:
    """Run the simulation with a live matplotlib display."""

    fig, ax = plt.subplots()
    img = ax.imshow(grid.cells, cmap=plt.cm.Blues, vmin=0, vmax=1)
    ax.set_title("Langton's Ant")
    plt.ion()
    plt.show()

    for state in simulate(grid, ant, steps):
        img.set_data(state)
        plt.gcf().canvas.draw()
        plt.pause(0.01)

    plt.ioff()
    plt.show()


def main() -> None:
    grid = Grid.empty(16)
    grid.cells[2, 5] = 1

    ant = Ant(x=4, y=5, direction=0)  # facing right
    visualize(grid, ant, steps=100)
    print("Final board:
", grid.cells)


if __name__ == "__main__":
    main()
