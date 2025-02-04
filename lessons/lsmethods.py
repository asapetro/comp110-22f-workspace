""""Methods."""
from __future__ import annotations


class Point:
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Constructs a point by giving x and y args."""
        self.x = x
        self.y = y

    def __str__(self) -> str:
        """Special method to represent object as string."""
        return f"{self.x}, {self.y}"

    def __mul__(self, factor: float) -> Point:
        """Overload the multiplication operator by factor."""
        return Point(self.x * factor, self.y * factor)

    # def scale(self, factor: float) -> Point:
    #     """Scale a Point's attributes by factor."""
    #     print("__mul__ was called")
    #     return Point(self.x * factor, self.y * factor)

    def __add__(self, rhs: Point) -> Point:
        print("__add__ was called")
        return Point(self.x +rhs.x, self.y + rhs.y)

    def __getitem__(self, index: int) -> float:
        """Overload the subscription notation."""
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else: 
            raise IndexError

a: Point = Point(1.0, 2.0)
b: Point = a * 2.0
c: Point = a + b
print(f"a: {a}")
print(f"b: {b}")
print(f"c: {c}")

print(a[0])
print(a[1])