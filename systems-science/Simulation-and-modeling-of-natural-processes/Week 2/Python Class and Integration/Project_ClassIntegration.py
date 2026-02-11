"""Numerical integration using simple quadrature rules.

This module demonstrates Riemann-sum and trapezoidal integration for a
smooth integrand. The algorithm discretizes the interval into N points,
then approximates the integral as a weighted sum of function values.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Protocol

import numpy as np


@dataclass(frozen=True)
class Bounds:
    """Closed interval [x_min, x_max]."""

    x_min: float
    x_max: float


@dataclass(frozen=True)
class IntegrationResult:
    """Result of a numerical integration run."""

    value: float
    n_points: int
    method: str


class Integrator(Protocol):
    """Strategy interface for numerical integration."""

    def integrate(
        self, func: Callable[[np.ndarray], np.ndarray], bounds: Bounds, n_points: int
    ) -> IntegrationResult: ...


class RiemannSumIntegrator:
    """Riemann-sum integrator.

    rule: "left" or "midpoint". The algorithm samples f(x) at the chosen
    points and multiplies the sum by dx.
    """

    def __init__(self, rule: str = "left") -> None:
        if rule not in {"left", "midpoint"}:
            raise ValueError("rule must be 'left' or 'midpoint'")
        self._rule = rule

    def integrate(
        self, func: Callable[[np.ndarray], np.ndarray], bounds: Bounds, n_points: int
    ) -> IntegrationResult:
        if n_points < 2:
            raise ValueError("n_points must be >= 2")

        x = np.linspace(bounds.x_min, bounds.x_max, n_points)
        dx = x[1] - x[0]

        if self._rule == "left":
            samples = x[:-1]
        else:
            samples = x[:-1] + 0.5 * dx

        value = float(np.sum(func(samples)) * dx)
        return IntegrationResult(value=value, n_points=n_points, method=f"riemann-{self._rule}")


class TrapezoidalIntegrator:
    """Trapezoidal rule integrator."""

    def integrate(
        self, func: Callable[[np.ndarray], np.ndarray], bounds: Bounds, n_points: int
    ) -> IntegrationResult:
        if n_points < 2:
            raise ValueError("n_points must be >= 2")

        x = np.linspace(bounds.x_min, bounds.x_max, n_points)
        y = func(x)
        value = float(np.trapz(y, x))
        return IntegrationResult(value=value, n_points=n_points, method="trapezoidal")


def integrand(x: np.ndarray) -> np.ndarray:
    """Target integrand: x^2 * exp(-x) * sin(x)."""

    return (x**2) * np.exp(-x) * np.sin(x)


def main() -> None:
    bounds = Bounds(1.0, 3.0)
    n_points = 200

    riemann = RiemannSumIntegrator(rule="left")
    trap = TrapezoidalIntegrator()

    r_result = riemann.integrate(integrand, bounds, n_points)
    t_result = trap.integrate(integrand, bounds, n_points)

    print(f"Riemann ({r_result.method}) N={r_result.n_points}: {r_result.value:.6f}")
    print(f"Trapezoidal N={t_result.n_points}: {t_result.value:.6f}")


if __name__ == "__main__":
    main()
