from abc import ABC
from Ship import Ship
from Display import Display
import pygame


class Board(ABC):
    """A abstract base class for boards"""

    def __init__(self, size=10, ship_sizes=[6, 4, 3, 3, 2]):
        self.size = size
        self.ship_sizes = ship_sizes
        self.ships_list = []
        self.hits_list = []
        self.misses_list = []

    def is_valid(self, ship):
        """Checks whether a ship would be a valid placement on the board"""
        for x, y in ship.coordinate_list:
            if x < 0 or y < 0 or x >= self.size or y >= self.size:
                return False
        for otherShip in self.ships_list:
            if self.ships_overlap(ship, otherShip):
                return False
        return True

    def add_ship(self, ship: Ship):
        """Adds a ship to the board"""
        if self.is_valid(ship):
            self.ships_list.append(ship)
            return True
        else:
            return False

    def remove_ship(self, ship):
        """Removes a ship from the board"""
        self.ships_list.remove(ship)

    def ships_overlap(self, ship1, ship2):
        """Checks whether two ships overlap"""
        for ship1_coord in ship1.coordinate_list:
            for ship2_coord in ship2.coordinate_list:
                if ship1_coord == ship2_coord:
                    return True
        return False

    def get_ship(self, x, y):
        """Gets a ship object from coordinates"""
        for ship in self.ships_list:
            if (x, y) in ship.coordinate_list:
                return ship
        return None

    def valid_target(self, x, y):
        """Checks whether a set of coordinates is a valid shot
        Coordinates are within the board, and shot hasn't previously been taken
        """
        if x not in range(self.size) or y not in range(self.size):
            return False
        for previous_shot in self.misses_list + self.hits_list:
            if (x, y) == previous_shot:
                return False
        return True

    def shoot(self, x, y,user):
        """Registers a shot on the board, saving to appropriate list"""
        if not self.valid_target(x, y):
            return False
        if user:
            Display.x1 = x
            Display.y1 = y
        else:
            Display.x2 = x
            Display.y2 = y


        for ship in self.ships_list:
            for ship_coordinate in ship.coordinate_list:
                if (x, y) == ship_coordinate:
                    if user:
                        Display.hit1 = True
                    else:
                        Display.hit2 = True
                    self.hits_list.append((x, y))
                    return True

        if user:
            Display.hit1 = False
        else:
            Display.hit2 = False
        self.misses_list.append((x, y))
        return True

    def colour_grid(self, colours, include_ships=True):
        """Calculates a colour representation of the board for display"""
        grid = [[colours["water"] for _ in range(self.size)]for _ in range(self.size)]
        if include_ships:
            for ship in self.ships_list:
                for x, y in ship.coordinate_list:
                    grid[y][x] = colours["ship"]

        for x, y in self.hits_list:
            grid[y][x] = colours["hit"]

        for x, y in self.misses_list:
            grid[y][x] = colours["miss"]

        return grid

    @property
    def gameover(self):
        """Checks to see if all the ships have been fully hit"""
        for ship in self.ships_list:
            for coordinate in ship.coordinate_list:
                if coordinate not in self.hits_list:
                    return False
        return True

    def __str__(self):
        """String representation of the board
        similar to colour grid but for printing
        """
        output = (("~" * self.size) + "\n") * self.size
        for ship in self.ships_list:
            for x, y in ship.coordinate_list:
                output[x + y * (self.size + 1)] = "S"
        return output

