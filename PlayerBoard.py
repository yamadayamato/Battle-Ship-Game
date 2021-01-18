
from itertools import zip_longest
from Direction import Direction
from Ship import Ship
from Board import Board
from Display import Display


class PlayerBoard(Board):
    """A Board for user input"""

    def __init__(self, display, board_size, ship_sizes):
        """Initialises the board by placing ships."""
        super().__init__(board_size, ship_sizes)
        self.display = display

        direction = Direction.NORTH
        while True:
            self.display.show(None, self)

            if self.ship_to_place:
                text = 'Click where you want your {} block long ship to be:'.format(
                    self.ship_to_place)
            else:
                text = 'Click again to rotate a ship, or elsewhere if ready.'
            self.display.show_text(text, lower=True)

            x, y = self.display.get_input()
            if x is not None and y is not None:
                ship = self.get_ship(x, y)
                if ship:
                    self.remove_ship(ship)
                    ship.rotate()
                    if self.is_valid(ship):
                        self.add_ship(ship)
                elif self.ship_to_place:
                    ship = Ship(x, y, direction, self.ship_to_place)
                    if self.is_valid(ship):
                        self.add_ship(ship)
                    else:
                        direction = direction.next
                else:
                    break

                if self.is_valid(ship):
                    self.add_ship(ship)

            Display.flip()

    @property
    def ship_to_place(self):
        """Returns a ship length that needs to be placed, if any"""
        placed_sizes = sorted(ship.length for ship in self.ships_list)
        sizes = sorted(self.ship_sizes)
        for placed, to_place in zip_longest(placed_sizes, sizes):
            if placed != to_place:
                return to_place
        return None
