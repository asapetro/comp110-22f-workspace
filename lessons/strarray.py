"""Examples of "Vectorized" operations via magic methods."""

from __future__ import annotations
from typing import Union


class StrArray:
    items: list[str]

    def __init__(self, items: list[str]):
        self.items = items

    def __repr__(self) -> str:
        return f"StrArray({self.items})"

    def __add__(self, rhs: Union[str, StrArray]) -> StrArray:
        result: StrArray = StrArray([])
        if isinstance(rhs, str):
            for name in self.items:
                name += rhs
                result.items.append(name)
        else:
            for i in range(len(self.items)):
                result.items.append(self.items[i] + rhs.items[i])
                # otherwise loop through each index of self's items
                # concatenate the corresponding value of rhs's items at same index
                # Append the resulting string to result's items list
        return result

a: StrArray = StrArray(["Armando", "Pete", "Leaky"])
b: StrArray = StrArray(["Bacot", "Nance", "Black"])
print(a)
print(a + "!")
print(a + " " + b)