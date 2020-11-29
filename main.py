"""
Main file for Magma Boy and Hydro Girl game.
"""

# import pygame and orther needed libraries
import sys
import pygame
from pygame.locals import *

# import needed classes for game
from board import Board
from game import Game
from players import Players
from controller import Controller


def main():
    # inialize the game
    clock = pygame.time.Clock()
    pygame.init()

    # initialize classes
    board = Board()
    # main game loop
    while True:
        # check for keyboard input
        for event in pygame.event.get():
            # if player closes the window
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # update the diaplay
        pygame.display.update()
        # run game at rate of 60 fps
        clock.tick(60)


if __name__ == '__main__':
    main()
