#!/usr/bin/env python3

from Game import Game
from Display import Display

if __name__ == "__main__":
    while True:
        d = Display()
        Game(d).play()
        # Game(d, 2, [1,1]).play()
        d.close()

        response = input("Replay? y/n: ").lower()
        while response not in ['y', 'n']:
            response = input("Must be y or n: ")
        if response == 'n':
            print("Thanks, goodbye.")
            break