import sys
import pygame
from pygame.locals import *

class LevelSelect():
    def __init__(self):
        self.load_images()

    def load_images(self):
        self.screen = pygame.image.load('data/level_select_screen/level_select_screen.png')
        self.level1_image = pygame.image.load('data/level_select_screen/level1.png')
        self.level1_image.set_colorkey((255, 0, 255))
        self.indicator_image = pygame.image.load('data/level_select_screen/indicator.png')
        self.indicator_image.set_colorkey((255, 0, 255))

    
