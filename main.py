"""
Main file for Magma Boy and Hydro Girl game.
"""

# import pygame and orther needed libraries
import sys
import pygame
from pygame.locals import *

# import classes
from game import Game
from board import Board
from character import MagmaBoy, HydroGirl
from controller import MagmaBoyController, HydroGirlController


def main():
    # inialize the game
    clock = pygame.time.Clock()
    pygame.init()

    # initialize board
    board = Board()
    level = "data/level0.txt"  # we can change level design by changing txt file
    board.load_map(level)
    board.load_images()
    board.make_solid_blocks()

    # initialize player
    hydro_girl = HydroGirl()
    magma_boy = MagmaBoy()

    # initialize game
    game = Game()

    # intialize controllers
    magma_boy_controller = MagmaBoyController(hydro_girl)
    hydro_girl_controller = HydroGirlController(hydro_girl)

    # main game loop
    while True:
        # draw board
        board.construct_board()

        hydro_girl.calc_movement()

        game.move_player(board, hydro_girl)

        game.draw_player(board, hydro_girl)

        game.draw_board(board)

        # check for keyboard input
        hydro_girl_controller.get_user_input()

        # run game at rate of 60 fps
        clock.tick(60)


if __name__ == '__main__':
    main()
