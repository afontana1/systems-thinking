"""Lotka-Volterra predator-prey simulation using explicit Euler.

Algorithm:
- Define population derivatives for prey and predators.
- Step forward in time with explicit Euler: y_{t+1} = y_t + dt * f(y_t).
- Plot population trajectories on log-log axes.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

import numpy as np
import matplotlib.pyplot as plt


@dataclass(frozen=True)
class LotkaVolterraParams:
    """Model parameters for the predator-prey system."""

    prey_birth: float
    predator_death: float
    predation_rate: float
    predator_reproduction: float


def derivatives(state: np.ndarray, params: LotkaVolterraParams) -> np.ndarray:
    """Compute derivatives [dPrey/dt, dPredator/dt]."""

    prey, predator = state
    d_prey = params.prey_birth * prey - params.predation_rate * prey * predator
    d_pred = -params.predator_death * predator + params.predator_reproduction * prey * predator
    return np.array([d_prey, d_pred], dtype=float)


class ExplicitEuler:
    """Explicit Euler integrator for ODE systems."""

    def integrate(
        self,
        deriv: Callable[[np.ndarray], np.ndarray],
        y0: np.ndarray,
        dt: float,
        steps: int,
    ) -> np.ndarray:
        y = np.zeros((steps, len(y0)), dtype=float)
        y[0] = y0
        for i in range(steps - 1):
            y[i + 1] = y[i] + dt * deriv(y[i])
        return y


def simulate(params: LotkaVolterraParams, y0: np.ndarray, dt: float, steps: int) -> tuple[np.ndarray, np.ndarray]:
    """Run the simulation and return (t, populations)."""

    t = np.arange(steps, dtype=float) * dt
    integrator = ExplicitEuler()
    populations = integrator.integrate(lambda s: derivatives(s, params), y0, dt, steps)
    return t, populations


def main() -> None:
    params = LotkaVolterraParams(
        prey_birth=1.0,
        predator_death=1.0,
        predation_rate=0.5,
        predator_reproduction=0.5,
    )

    dt = 0.001
    steps = 30000  # matches original length: total time = steps * dt
    y0 = np.array([2.0, 3.0], dtype=float)

    t, populations = simulate(params, y0, dt, steps)
    prey = populations[:, 0]
    predator = populations[:, 1]

    plt.loglog(t, prey, linewidth=2.0, label="Prey (antelopes)")
    plt.loglog(t, predator, linewidth=2.0, label="Predators (cheetahs)")
    plt.xlabel("Time")
    plt.ylabel("Population")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
