"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730575054"


class Simpy:
    """Simpy class."""
    values: list[float]

    def __init__(self, a_list: list[float]):
        """Initialize the values attribute to the argument."""
        self.values = []
        for value in a_list:
            self.values.append(value)

    def __repr__(self) -> str:
        """Converts Simpy object to a str representation."""
        return f"Simpy({self.values})"

    def fill(self, value: float, num: int) -> None:
        """Fills values with value a num amount of times."""
        self.values = list()
        for _ in range(0, num):
            self.values.append(value)

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fills values with range of values."""
        assert step != 0.0
        self.values = list()
        add_value: float = 0.0
        add_value = start
        i = 0
        while i < (stop - start) / step:
            self.values.append(add_value)
            add_value += step
            i += 1

    def sum(self) -> float:
        """Sums values."""
        return sum(self.values)

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Adds ability to us addition operator with Simpy objects and floats."""
        if type(rhs) == Simpy:
            assert len(self.values) == len(rhs.values)
        result = Simpy([])
        if type(rhs) == float:
            for i in range(0, len(self.values)):
                result.values.append(self.values[i] + rhs)
        else:
            for i in range(0, len(self.values)):
                result.values.append(self.values[i] + rhs.values[i])
        return result

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Adds ability to use power operator on Simpy objects and floats."""
        if type(rhs) == Simpy:
            assert len(self.values) == len(rhs.values)
        result = Simpy([])
        if type(rhs) == float:
            for i in range(0, len(self.values)):
                result.values.append(self.values[i] ** rhs)
        else:
            for i in range(0, len(self.values)):
                result.values.append(self.values[i] ** rhs.values[i])
        return result

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Adds ability to produce mask."""
        result: list[bool] = list()
        if type(rhs) == float:
            for i in range(len(self.values)):
                result.append(self.values[i] == rhs)
        else:
            for i in range(len(self.values)):
                result.append(self.values[i] == rhs.values[i])
        return result

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Produces mask."""
        result: list[bool] = list()
        if type(rhs) == float:
            for i in range(len(self.values)):
                result.append(self.values[i] > rhs)
        else:
            for i in range(len(self.values)):
                result.append(self.values[i] > rhs.values[i])
        return result

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Adds subscription notation."""
        result = Simpy([])
        if type(rhs) == int:
            return self.values[rhs]
        else:
            for i in range(0, len(self.values)):
                if rhs[i]:
                    result.values.append(self.values[i])
        return result