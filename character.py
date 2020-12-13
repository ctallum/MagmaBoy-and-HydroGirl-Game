import sys
import pygame
from pygame.locals import *

class Character:
    def __init__(self):
        self.image = pygame.image.load('data/player_images/player.png')
        self.moving_right = False
        self.moving_left = False
        self.jumping = False #here
        self.y_velocity = 0
        self.air_timer = 0
        self.rect = pygame.Rect(16, 350, self.image.get_width(), self.image.get_height())
        self.is_alive = True

    def calc_movement(self):
        # Motion constants
        LATERAL_SPEED = 3
        JUMP_SPEED = -5
        GRAVITY = 0.2
        TERMINAL_VELOCITY = 3

        # set initially to not moving
        self.movement = [0, 0]
        # calculate horizontal movement
        if self.moving_right:
            self.movement[0] += LATERAL_SPEED
        if self.moving_left:
            self.movement[0] -= LATERAL_SPEED

        # calculate vertical movement
        if self.jumping:
            self.y_velocity = JUMP_SPEED
            self.jumping = False
        self.movement[1] += self.y_velocity
        self.y_velocity += GRAVITY
        # establish terminal velocity of 3px/frame
        if self.y_velocity > TERMINAL_VELOCITY:
            self.y_velocity = TERMINAL_VELOCITY

    def reset_character(self):
        self.moving_right = False
        self.moving_left = False
        self.y_velocity = 0
        self.air_timer = 0
        self.rect = pygame.Rect(16, 350, self.image.get_width(), self.image.get_height())
        self.is_alive = True

    def is_dead(self):
        return not self.is_alive


class MagmaBoy(Character):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('data/player_images/magmaboy.png')
        self.side_image = pygame.image.load('data/player_images/magmaboyside.png')
        self.type = "magma"


class HydroGirl(Character):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('data/player_images/hydrogirl.png')
        self.side_image = pygame.image.load('data/player_images/hydrogirlside.png')
        self.type = "water"

