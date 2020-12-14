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
from gates import Gates
from doors import FireDoor, WaterDoor
from level_select import LevelSelect

def main():
    pygame.init()
    game = Game()

    game.loading_screen(Controller)

    select_level(game)

def select_level(game):
    level_select = LevelSelect()
    level = game.user_select_level(level_select, Controller)
    run_game(game, level)


def run_game(game, level): 
    clock = pygame.time.Clock()

    hydro_girl = HydroGirl()
    magma_boy = MagmaBoy()

    magma_boy_controller = MagmaBoyController(magma_boy)
    hydro_girl_controller = HydroGirlController(hydro_girl)

    if level == "level1":

        board = Board('data/level1.txt')
        gates = Gates((300, 128), [(425,168), (150,168)])

        fire_door = FireDoor((64, 48), (64, 48), (48, 16))
        water_door = WaterDoor((128, 48), (128, 48), (112, 16))
    
    if level == "level2":
        pass


    # main game loop
    while True:
        game.draw_board(board)

        game.draw_gates(gates)

        events = pygame.event.get()

        Controller.check_for_end(events)

        if Controller.press_key(events, K_ESCAPE):
            select_level(game)

        magma_boy_controller.control_player(events)
        hydro_girl_controller.control_player(events)

        magma_boy.calc_movement()
        hydro_girl.calc_movement()

        game.move_player(board, gates, [magma_boy, hydro_girl])

        game.check_for_death(board, [magma_boy, hydro_girl])

        game.check_for_gate_press(gates, [magma_boy, hydro_girl])

        game.draw_doors([fire_door, water_door])
        game.check_for_door_open(fire_door, magma_boy)
        game.check_for_door_open(water_door, hydro_girl)

        game.draw_player([magma_boy, hydro_girl])

        if hydro_girl.is_dead() or magma_boy.is_dead():
            action = game.death_sequence([magma_boy, hydro_girl],Controller)
            if action == "continue":
                pass
            if action == "escape":
                select_level(game)

        if game.level_is_done([fire_door, water_door]):
            game.win_sequence(Controller)
            select_level(game)

        game.refresh_window()

        clock.tick(60)

if __name__ == '__main__':
    main()
