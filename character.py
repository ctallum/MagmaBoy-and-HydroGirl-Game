import sys
import pygame
from pygame.locals import *

class Character:
    def __init__(self):
        self.image = pygame.image.load('data/player_images/player.png')
        self.moving_right = False
        self.moving_left = False
        self.y_velocity = 0
        self.air_timer = 0
        self.rect = pygame.Rect(0, 300, self.image.get_width(), self.image.get_height())
        self.type = None
        self.state = 1 # 1 = alive, 0 = dead

    def calc_movement(self):
        # set initially to not moving
        self.movement = [0, 0]
        # calculate horizontal movement
        if self.moving_right:
            self.movement[0] += 2.5
        if self.moving_left:
            self.movement[0] -= 2.5

        # calculate vertical movement
        self.movement[1] += self.y_velocity
        self.y_velocity += 0.2
        # establish terminal velocity of 3px/frame
        if self.y_velocity > 3:
            self.y_velocity = 3


class MagmaBoy(Character):
    def __init__(self):
        super().__init__()
        self.type = 'fire'
        self.controls = "wasd"


class HydroGirl(Character):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('data/player_images/hydrogirl.png')
        self.image.set_colorkey((255, 0, 255))
        self.type = 'water'
        self.controls = "arrows"
