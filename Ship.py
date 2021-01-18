from Direction import Direction

class Ship:
    """An object to store the data of one ship"""

    def __init__(self, x, y, d, l):
        self.location = (x, y)
        self.direction = d
        self.length = l

    @property
    def coordinate_list(self):
        """Calculates the list of coordinates that the ship is located over"""
        x, y = self.location
        if self.direction == Direction.NORTH:
            return [(x, y - i) for i in range(self.length)]
        elif self.direction == Direction.EAST:
            return [(x + i, y) for i in range(self.length)]
        elif self.direction == Direction.SOUTH:
            return [(x, y + i) for i in range(self.length)]
        elif self.direction == Direction.WEST:
            return [(x - i, y) for i in range(self.length)]


    def rotate(self):
        """Rotates the ship"""
        self.direction = self.direction.next

    def __repr__(self):
        """A nice representation of the Ship object, for debugging"""
        return "<Ship Object: ({},{}), {}, Length {}>".format(
            *self.location, self.direction, self.length)

