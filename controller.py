import sys
import pygame
from pygame.locals import *

class Controller:
    def __init__(self, player):
        self.player = player

    def get_user_input(self, events):

        for event in events:
            # if player closes the window
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == self.controls["right"]:
                    self.player.moving_right = True
                if event.key == self.controls["left"]:
                    self.player.moving_left = True
                if event.key == self.controls["up"]:
                    if self.player.air_timer < 6:
                        self.player.y_velocity = -5.5
            if event.type == KEYUP:
                if event.key == self.controls["right"]:
                    self.player.moving_right = False
                if event.key == self.controls["left"]:
                    self.player.moving_left = False


class MagmaBoyController(Controller):
    def __init__(self, player):
        super().__init__(player)
        self.controls = {
            "left": K_a,
            "right": K_d,
            "up": K_w
        }

class HydroGirlController(Controller):
    def __init__(self, player):
        super().__init__(player)
        self.controls = {
            "left": K_LEFT,
            "right": K_RIGHT,
            "up": K_UP
        }


