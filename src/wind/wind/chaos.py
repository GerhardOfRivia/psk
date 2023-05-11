#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
import logging
import numpy as np
from typing import Tuple


class Lorenz:
    """Lorenz Attractor

    Description:
        Lorenz attractor is ordinary differential equation (ODE) of 3rd order system.
        In 1963, E. Lorenz developed a simplified mathematical model for
        atmospheric convection.

        Lorenz equations are:
            dx/dt = sigma * (y - x)
            dy/dt = rho * x - y - x * z
            dz/dt = x * y - beta * z

        where:
            beta, rho and sigma - are Lorenz system parameters.
        default values for parameters are:
            beta = 8/3,
            rho = 28,
            sigma = 10.

        If rho < 1  then there is only one equilibrium point,
        which is at the origin. This point corresponds to no convection.

    Examples
    --------
    >>> coordinates = (0, 1, -1)
    >>> model = Lorenz(num_points=1)
    >>> output = model.attractor(*coordinates)
    >>> print(output)
    (10, -1, 2.6666666666666665)
    >>> model = Lorenz(num_points=10, init_point=(0.1, 0, -0.1), step=100)
    >>> print(model.get_coordinates())
    [[ 0.1         0.         -0.1       ]
     [ 0.09        0.0281     -0.09733333]
     [ 0.08381     0.0531066  -0.09471249]
     [ 0.08073966  0.07612171 -0.09214231]
     [ 0.08027787  0.098042   -0.08962372]
     [ 0.08205428  0.11961133 -0.08715505]
     [ 0.08580998  0.14146193 -0.08473277]
     [ 0.09137518  0.16414681 -0.08235184]
     [ 0.09865234  0.18816564 -0.0800058 ]
     [ 0.10760367  0.21398557 -0.07768669]]

    See Also
    --------
    Chaotic theory:
    https://en.wikipedia.org/wiki/Chaos_theory
    Attractors (dynamical systems):
    https://en.wikipedia.org/wiki/Attractor
    """

    def __init__(
        self,
        num_points: int,
        init_point: Tuple[float, float, float] = (0, 0, 0),
        step: float = 1,
        **kwargs: dict,
    ):
        self.num_points = num_points
        self.init_point = init_point
        self.step = step
        self.kwargs = kwargs

    def get_coordinates(self):
        return np.array(list(next(self)))

    def __len__(self):
        return self.num_points

    def __iter__(self):
        return self

    def __next__(self):
        points = self.init_point
        for i in range(self.num_points):
            try:
                yield points
                next_points = self.attractor(*points, **self.kwargs)
                points = tuple(prev + curr / self.step for prev, curr in zip(points, next_points))
            except OverflowError:
                logging.error(f"Cannot do the next step because of floating point overflow. Step: {i}")
                break

    @staticmethod
    def attractor(
        x: float,
        y: float,
        z: float,
        sigma: float = 10,
        beta: float = 8 / 3,
        rho: float = 28,
    ) -> Tuple[float, float, float]:
        """Calculate the next coordinate X, Y, Z for 3rd-order Lorenz system
        Parameters
        ----------
        x, y, z : float
            Input coordinates X, Y, Z respectively.
        sigma, beta, rho : float
            Lorenz system parameters. Default:
                - sigma = 10,
                - beta = 8/3,
                - rho = 28,
        See Also
        -----
        https://en.wikipedia.org/wiki/Lorenz_system
        """
        x_out = sigma * (y - x)
        y_out = rho * x - y - x * z
        z_out = x * y - beta * z
        return x_out, y_out, z_out

    def update_attributes(self, **kwargs):
        """Update chaotic system parameters."""
        for key in kwargs:
            if key in self.__dict__ and not key.startswith("_"):
                self.__dict__[key] = kwargs.get(key)
