"""2D Lattice Boltzmann (D2Q9) simulation with a cylindrical obstacle.

Algorithm:
- Initialize populations (f) from equilibrium with a small velocity field.
- For each step:
  1. Compute density (rho) and velocity (u).
  2. Compute equilibrium distribution (feq).
  3. Collision: f <- f - omega * (f - feq).
  4. Streaming: shift populations along lattice directions.
  5. Bounce-back on obstacle for no-slip boundary.
- Optionally save velocity magnitude images.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


C = np.array(
    [
        [1, 1],
        [1, 0],
        [1, -1],
        [0, 1],
        [0, 0],
        [0, -1],
        [-1, 1],
        [-1, 0],
        [-1, -1],
    ],
    dtype=int,
)
W = np.array([1 / 36, 1 / 9, 1 / 36, 1 / 9, 4 / 9, 1 / 9, 1 / 36, 1 / 9, 1 / 36], dtype=float)
OPPOSITE = np.array([8, 7, 6, 5, 4, 3, 2, 1, 0], dtype=int)


@dataclass(frozen=True)
class LBMConfig:
    nx: int = 400
    ny: int = 100
    steps: int = 50
    reynolds: float = 10.0
    u0: float = 0.04
    obstacle_radius: float | None = None
    save_every: int = 5


class LatticeBoltzmannSimulator:
    def __init__(self, config: LBMConfig) -> None:
        self.config = config
        self.nx = config.nx
        self.ny = config.ny
        self.r = config.obstacle_radius or (self.ny / 9.0)
        self.cx = self.nx // 4
        self.cy = self.ny // 2
        self.nu = config.u0 * self.r / config.reynolds
        self.omega = 1.0 / (3.0 * self.nu + 0.5)

        self.f = np.zeros((9, self.ny, self.nx), dtype=float)
        self._init_state()
        self.obstacle = self._cylinder_mask()

    def _cylinder_mask(self) -> np.ndarray:
        y, x = np.ogrid[: self.ny, : self.nx]
        return (x - self.cx) ** 2 + (y - self.cy) ** 2 <= self.r**2

    def _init_state(self) -> None:
        y = np.arange(self.ny)
        yy, _ = np.meshgrid(y, np.arange(self.nx), indexing="ij")
        u = np.zeros((2, self.ny, self.nx), dtype=float)
        u[0] = self.config.u0 * (1.0 + 1e-4 * np.sin(yy / (self.ny - 1) * 2 * np.pi))
        u[1] = 0.0

        rho = np.ones((self.ny, self.nx), dtype=float)
        self.f = self._equilibrium(rho, u)

    def _equilibrium(self, rho: np.ndarray, u: np.ndarray) -> np.ndarray:
        cu = 3.0 * (
            C[:, 0][:, None, None] * u[0][None, :, :]
            + C[:, 1][:, None, None] * u[1][None, :, :]
        )
        u2 = u[0] ** 2 + u[1] ** 2
        feq = W[:, None, None] * rho[None, :, :] * (1 + cu + 0.5 * cu**2 - 1.5 * u2)
        return feq

    def _macroscopic(self) -> tuple[np.ndarray, np.ndarray]:
        rho = np.sum(self.f, axis=0)
        u = np.zeros((2, self.ny, self.nx), dtype=float)
        u[0] = np.sum(self.f * C[:, 0][:, None, None], axis=0) / rho
        u[1] = np.sum(self.f * C[:, 1][:, None, None], axis=0) / rho
        return rho, u

    def step(self) -> np.ndarray:
        rho, u = self._macroscopic()
        feq = self._equilibrium(rho, u)
        self.f = self.f - self.omega * (self.f - feq)

        for i, (cx, cy) in enumerate(C):
            self.f[i] = np.roll(self.f[i], shift=cx, axis=1)
            self.f[i] = np.roll(self.f[i], shift=cy, axis=0)

        self.f[:, self.obstacle] = self.f[OPPOSITE][:, self.obstacle]
        return u

    def run(self, output_dir: Path | None = None) -> None:
        output_dir = output_dir or (Path(__file__).parent / "Diagram of the flow")
        output_dir.mkdir(exist_ok=True)

        for step in range(self.config.steps):
            u = self.step()
            if self.config.save_every and step % self.config.save_every == 0:
                self._save_velocity_plot(output_dir, step, u)

    def _save_velocity_plot(self, output_dir: Path, step: int, u: np.ndarray) -> None:
        plt.clf()
        speed = np.sqrt(u[0] ** 2 + u[1] ** 2)
        plt.imshow(speed, cmap=cm.Reds, origin="lower")
        plt.colorbar(label="Speed")
        plt.title(f"Velocity magnitude (step {step})")
        plt.savefig(output_dir / f"vel.{step:06}.png", dpi=150)


def main() -> None:
    config = LBMConfig(steps=50, save_every=5)
    sim = LatticeBoltzmannSimulator(config)
    sim.run()


if __name__ == "__main__":
    main()
