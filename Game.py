import random
from AIBoard import AIBoard
from PlayerBoard import PlayerBoard
from Display import Display

class Game:
    """The overall class to control the game"""

    def __init__(self, display, size=10, ship_sizes=[6, 4, 3, 3, 2]):
        """Sets up the game by generating two Boards"""
        self.display = display
        self.board_size = size
        self.ai_board = AIBoard(size, ship_sizes)
        self.player_board = PlayerBoard(display, size, ship_sizes)

    def play(self):
        """The main game loop, alternating shots until someone wins"""
        print("Play starts")
        print("1)User Ship Are in Grey color")
        print("2)Red Block represents hit")
        print("3)Black Block represents Miss")
        while not self.gameover:
            if self.player_shot():
                self.ai_shot()
            self.display.show(self.ai_board, self.player_board)
            self.display.show_text("Click to guess:")
            Display.flip()

    def ai_shot(self):
        """The AI's shot selection just randomly selects coordinates"""
        x, y = -1, -1
        while not self.player_board.valid_target(x, y):
            x = random.randint(0, self.board_size - 1)
            y = random.randint(0, self.board_size - 1)
        self.player_board.shoot(x, y,False)

    def player_shot(self):
        """Uses input to decide if a shot is valid or not"""
        x, y = self.display.get_input()
        if self.ai_board.valid_target(x, y):
            self.ai_board.shoot(x, y,True)
            return True
        else:
            return False

    @property
    def gameover(self):
        """Determines and prints the winner"""
        if self.ai_board.gameover:
            print("Congratulations you won")
            return True
        elif self.player_board.gameover:
            print("Congratulations you lost")
            return True
        else:
            return False