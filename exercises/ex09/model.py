"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi, sqrt

__author__ = "730575054"


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)

    def distance(self, a_cell: Point) -> float:
        """Returns distance between Point object method was called on and Point object passed in as a parameter."""
        cell_dist: int
        cell_dist = sqrt(((self.x - a_cell.x) ** 2) + ((self.y - a_cell.y) ** 2))
        return cell_dist


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = constants.VULNERABLE

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction

    def contract_disease(self) -> None:
        """."""
        self.sickness = constants.INFECTED 

    def is_vulnerable(self) -> bool:
        """."""
        if self.sickness == constants.VULNERABLE:
            return True
        else:
            return False

    def is_infected(self) -> bool:
        """."""
        if self.sickness >= constants.INFECTED:
            return True
        else:
            return False
    
    def color(self) -> str:
        """."""
        if self.is_infected():
            return "cyan"
        if self.is_immune():
            return "blue"
        return "gray"

    def tick(self) -> None:
        """."""
        self.location = self.location.add(self.direction)
        if self.is_infected():
            self.sickness += 1
        if self.sickness > constants.RECOVERY_PERIOD:
            self.immunize()

    def contact_with(self, a_cell: Cell) -> None:
        """Checks contact between cells."""
        if self.is_infected() and a_cell.is_vulnerable():
            a_cell.contract_disease()
        if a_cell.is_infected() and self.is_vulnerable():
            self.contract_disease()

    def immunize(self) -> None:
        """Makes cell immune."""
        self.sickness = constants.IMMUNE

    def is_immune(self) -> bool:
        """Checks if cell is immune."""
        if self.sickness == constants.IMMUNE:
            return True


class Model:
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0
    immune_num: int = 0

    def __init__(self, cells: int, speed: float, infect_num: int, immune_num: int = 0):
        """Initialize the cells with random locations and directions."""
        self.population = []
        for i in range(0, cells):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            self.population.append(cell)
        for i in range(0, infect_num):
            self.population[i].contract_disease()
        for e in range(infect_num, infect_num + immune_num):
            self.population[e].immunize()

        if infect_num >= cells:
            raise ValueError("Some number of cells must be uninfected.")
        if infect_num <= 0:
            raise ValueError("Some number of cells must be infected.")
        if immune_num >= cells:
            raise ValueError("Some number of cells must be unimmune.")
        if immune_num <= 0:
            raise ValueError("Some number of cells must be immmune.")
    
    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)
        self.check_contacts()

    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = 2.0 * pi * random()
        direction_x: float = cos(random_angle) * speed
        direction_y: float = sin(random_angle) * speed
        return Point(direction_x, direction_y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1.0
        if cell.location.x < constants.MIN_X:
            cell.location.x = constants.MIN_X
            cell.direction.x *= -1
        if cell.location.y > constants.MAX_Y:
            cell.location.y = constants.MAX_Y
            cell.direction.y *= -1
        if cell.location.y < constants.MIN_Y:
            cell.location.y = constants.MIN_Y
            cell.direction.y *= -1

    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        for cell in self.population:
            if cell.is_infected():
                return False
        return True

    def check_contacts(self) -> None:
        """Test whether any two Cell values come in “contact” with one another."""
        for i in range(0, len(self.population)):
            for x in range(i + 1, len(self.population)):
                if self.population[i].location.distance(self.population[x].location) < constants.CELL_RADIUS:
                    self.population[i].contact_with(self.population[x])
            