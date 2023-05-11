#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
"""
"""
import pandas as pd
from .chaos import Lorenz


class Wind:
    def __init__(self, points: int = 1, step: float = 1):
        """TODO"""
        self.points = points
        self.step = step
        self.model = Lorenz(num_points=points, init_point=(0, 0, 0), step=step)

    @property
    def df(self):
        try:
            ndarray = self.model.get_coordinates()
            return pd.DataFrame(ndarray, columns=["X", "Y", "Z"])
        finally:
            next(self.model)
