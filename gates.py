import sys
import pygame
from pygame.locals import *

class Gates:
    def __init__(self, gate_location, plate_locatons):
        self.gate_location = gate_location
        self.plate_locations = plate_locatons
        self.plate_is_pressed = False
        self._gate_is_open = False

        self.load_images()
        self.make_rects()

    def load_images(self):
        """
        Load images for gate and plates
        """
        self.gate_image = pygame.image.load('data/gates_and_plates/gate.png')
        self.gate_image.set_colorkey((255, 0, 255))
        self.plate_image = pygame.image.load('data/gates_and_plates/plate.png')
        self.plate_image.set_colorkey((255, 0, 255))

    def make_rects(self):
        """
        Make pygame rects for gate and plates
        """
        self._gate = pygame.Rect(self.gate_location[0], self.gate_location[1],
                                self.gate_image.get_width(), self.gate_image.get_height())
        self._plates = []
        for location in self.plate_locations:
            self._plates.append(
                pygame.Rect(location[0], location[1], 
                self.plate_image.get_width(), self.plate_image.get_height())
            )

    def try_open_gate(self):
        """
        If person is on button, open gate, otherwise, keep gate closed
        """
        if self.plate_is_pressed and not self._gate_is_open:
            self.gate_location = (self.gate_location[0], self.gate_location[1] - 32)
            self._gate.y -= 32
            self._gate_is_open = True
        if not self.plate_is_pressed and self._gate_is_open:
            self.gate_location = (self.gate_location[0], self.gate_location[1] + 32)
            self._gate.y += 32
            self._gate_is_open = False

    def get_solid_blocks(self):
        """
        Return list of solid blocks
        """
        return [self._gate]

    def get_plates(self):
        """
        Return list of plate rects
        """
        return self._plates
