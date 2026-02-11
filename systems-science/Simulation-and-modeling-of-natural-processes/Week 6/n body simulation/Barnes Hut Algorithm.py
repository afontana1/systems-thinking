"""Barnes-Hut N-body simulation (2D) with a quadtree.

Algorithm:
- Build a quadtree that stores total mass and center of mass in each node.
- For each body, approximate distant nodes as a single mass if s / d < theta.
- Update velocity and position with a symplectic Euler step.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Optional

import numpy as np
import matplotlib.pyplot as plt


@dataclass
class Body:
    mass: float
    position: np.ndarray  # shape (2,)
    velocity: np.ndarray  # shape (2,)


@dataclass
class Quad:
    center: np.ndarray  # shape (2,)
    half_size: float

    def contains(self, pos: np.ndarray) -> bool:
        return np.all(np.abs(pos - self.center) <= self.half_size)

    def subdivide(self) -> list["Quad"]:
        hs = self.half_size / 2.0
        offsets = np.array([
            [-hs, -hs],
            [hs, -hs],
            [-hs, hs],
            [hs, hs],
        ])
        return [Quad(self.center + o, hs) for o in offsets]


class Node:
    def __init__(self, quad: Quad) -> None:
        self.quad = quad
        self.body: Optional[Body] = None
        self.children: list[Optional[Node]] = [None, None, None, None]
        self.mass = 0.0
        self.com = np.zeros(2, dtype=float)

    def is_leaf(self) -> bool:
        return all(child is None for child in self.children)

    def insert(self, body: Body) -> None:
        if self.body is None and self.is_leaf():
            self.body = body
            self.mass = body.mass
            self.com = body.position.copy()
            return

        if self.is_leaf():
            existing = self.body
            self.body = None
            self._subdivide()
            if existing is not None:
                self._insert_into_child(existing)

        self._insert_into_child(body)
        self._recompute_mass()

    def _subdivide(self) -> None:
        quads = self.quad.subdivide()
        self.children = [Node(q) for q in quads]

    def _insert_into_child(self, body: Body) -> None:
        for child in self.children:
            if child and child.quad.contains(body.position):
                child.insert(body)
                return

    def _recompute_mass(self) -> None:
        mass = 0.0
        com = np.zeros(2, dtype=float)
        for child in self.children:
            if child and child.mass > 0.0:
                mass += child.mass
                com += child.mass * child.com
        if mass > 0.0:
            com /= mass
        self.mass = mass
        self.com = com


def compute_force(body: Body, node: Node, theta: float, G: float, softening: float) -> np.ndarray:
    if node.mass == 0.0 or (node.is_leaf() and node.body is body):
        return np.zeros(2, dtype=float)

    dx = node.com - body.position
    dist = np.linalg.norm(dx) + softening

    if node.is_leaf() or (node.quad.half_size * 2.0) / dist < theta:
        return G * body.mass * node.mass * dx / (dist**3)

    force = np.zeros(2, dtype=float)
    for child in node.children:
        if child is not None:
            force += compute_force(body, child, theta, G, softening)
    return force


def build_tree(bodies: list[Body], domain: Quad) -> Node:
    root = Node(domain)
    for body in bodies:
        if domain.contains(body.position):
            root.insert(body)
    return root


def simulate(
    bodies: list[Body],
    steps: int,
    dt: float,
    theta: float,
    G: float,
    softening: float,
    sample_every: int,
    output_dir: Path,
) -> None:
    output_dir.mkdir(exist_ok=True)
    domain = Quad(center=np.array([0.5, 0.5]), half_size=0.5)

    for step in range(steps):
        tree = build_tree(bodies, domain)
        for body in bodies:
            force = compute_force(body, tree, theta, G, softening)
            accel = force / body.mass
            body.velocity += accel * dt
            body.position += body.velocity * dt

        if sample_every and step % sample_every == 0:
            fig, ax = plt.subplots()
            ax.set_aspect("equal")
            ax.scatter([b.position[0] for b in bodies], [b.position[1] for b in bodies], s=4)
            ax.set_xlim(0.0, 1.0)
            ax.set_ylim(0.0, 1.0)
            fig.savefig(output_dir / f"bodies_{step:06}.png", dpi=150)
            plt.close(fig)


def main() -> None:
    rng = np.random.default_rng(1)
    num_bodies = 20
    mass = 1.0
    radius = 0.1
    speed = 0.1

    positions = rng.random((num_bodies, 2)) * 2 * radius + 0.5 - radius
    bodies: list[Body] = []
    for pos in positions:
        if np.linalg.norm(pos - np.array([0.5, 0.5])) <= radius:
            r = pos - np.array([0.5, 0.5])
            tangent = np.array([-r[1], r[0]])
            velocity = tangent / (np.linalg.norm(tangent) + 1e-8) * speed
            bodies.append(Body(mass=mass, position=pos, velocity=velocity))

    simulate(
        bodies=bodies,
        steps=100,
        dt=0.001,
        theta=0.5,
        G=4e-6,
        softening=1e-4,
        sample_every=10,
        output_dir=Path("."),
    )


if __name__ == "__main__":
    main()
