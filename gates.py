import sys
import pygame
from pygame.locals import *

class Gates:
    def __init__(self):
        self.plate_is_pressed = False
        self.gate_is_open = False

        self.load_images()
        self.make_rects()

    def load_images(self):
        self.gate_image = pygame.image.load('data/gates_and_plates/gate.png')
        self.plate_image = pygame.image.load('data/gates_and_plates/plate.png')
    
    def make_rects(self):
        self.gate = pygame.Rect(self.gate_location[0], self.gate_location[1],
                                self.gate_image.get_width(), self.gate_image.get_height())
        self.plates = []
        for location in self.plate_locations:
            self.plates.append(
                pygame.Rect(location[0], location[1], 
                self.plate_image.get_width(), self.plate_image.get_height())
            )

    def try_open_gate(self):
        if self.plate_is_pressed and not self.gate_is_open:
            self.gate_location = (self.gate_location[0], self.gate_location[1] - 40)
            self.gate.y -= 40
            self.gate_is_open = True
        if not self.plate_is_pressed and self.gate_is_open:
            self.gate_location = (self.gate_location[0], self.gate_location[1] + 40)
            self.gate.y += 40
            self.gate_is_open = False

    def get_solid_blocks(self):
        return [self.gate]

    def get_plates(self):
        return self.plates

class GatesLevel1(Gates):
    def __init__(self):
        self.gate_location = (300, 128)
        self.plate_locations = [(425,168), (150,168)]
        super().__init__()

class GatesLevel2(Gates):
    pass