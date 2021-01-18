from enum import Enum


class Direction(Enum):
    """A enum for storing the four points of the compass"""
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

    @property
    def next(self):
        """Returns the next point of the compass, for rotations"""
        return Direction((self.value + 1) % 4)

