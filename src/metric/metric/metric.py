#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
"""
"""

from abc import ABC, abstractmethod
from threading import RLock
from typing import Union


class Metric(ABC):
    """A simple metric class"""

    def __init__(self, metric_name: str):
        """
        :param metric_name: str
        """
        self.metric_name = metric_name
        self._data = {}
        self._lock = RLock()

    @abstractmethod
    def add(self, label_values: dict, metric: Union[int, float]) -> None:
        """
        :param label_values: dict
        :param metric: Union[int, float]
        :return:
        """
        raise NotImplementedError()

    @abstractmethod
    def export(self) -> str:
        """
        Metrics can be exposed to Prometheus using a simple text-based exposition format
        https://prometheus.io/docs/instrumenting/exposition_formats/
        :return:
        """
        raise NotImplementedError()
