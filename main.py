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
from controller import MagmaBoyController, HydroGirlController, Controller


def main():
    # inialize pygame
    pygame.init()
    clock = pygame.time.Clock()
    
    # initialize all classes used in game
    game = Game()
    
    board = Board('data/level0.txt')

    hydro_girl = HydroGirl()
    magma_boy = MagmaBoy()

    magma_boy_controller = MagmaBoyController(magma_boy)
    hydro_girl_controller = HydroGirlController(hydro_girl)


    # loading screen
    game.loading_screen(Controller)

    # main game loop
    while True:
        game.draw_board(board)

        events = pygame.event.get()

        magma_boy_controller.get_user_input(events)
        hydro_girl_controller.get_user_input(events)
        
        magma_boy.calc_movement()
        hydro_girl.calc_movement()
        
        game.move_player(board, magma_boy)
        game.move_player(board, hydro_girl)

        game.check_for_death(board, magma_boy)
        game.check_for_death(board, hydro_girl)

        game.draw_player(magma_boy)
        game.draw_player(hydro_girl)

        if hydro_girl.is_dead() or magma_boy.is_dead():
            # show death screen
            
            game.death_sequence(board,[magma_boy, hydro_girl],Controller)


        game.refresh_window()

        clock.tick(60)


if __name__ == '__main__':
    main()
