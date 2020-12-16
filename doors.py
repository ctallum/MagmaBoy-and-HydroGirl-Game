import sys
import pygame
from pygame.locals import *

class Doors:
    def __init__(self):
        self.player_at_door = False
        self._height_raised = 0
        self._door_open = False

        self.load_images()
        self.make_rects()
    
    def load_images(self):
        """
        Load the images for the door
        """
        self.frame_image = pygame.image.load("data/door_images/door_frame.png")
        self.frame_image.set_colorkey((255, 0, 255))
        self.door_background = pygame.image.load("data/door_images/door_background.png")
        

    def make_rects(self):
        """
        Create pygame rect for the door
        """
        self._rect = pygame.Rect(self.door_location[0], self.door_location[1],
                                self.door_image.get_width(), self.door_image.get_height())

    def get_door(self):
        """
        Return a rect containing the location and size of the door
        """
        return self._rect

    def is_door_open(self):
        """
        Return a boolean containing the status of the door
        """
        return self._door_open

    def try_raise_door(self):
        """
        Try to raise door if conditions are met. 

        Raise door if player is at the door and the door is closed.
        """
        DOOR_SPEED = 1.5
        if self.player_at_door and not self._door_open:
            self.door_location = (self.door_location[0], self.door_location[1] - DOOR_SPEED)
            self._height_raised += DOOR_SPEED
            if self._height_raised >= 31:
                self._door_open = True
        elif not self.player_at_door:
            if self._height_raised > 0:
                self._height_raised -= DOOR_SPEED
                self.door_location = (self.door_location[0], self.door_location[1] + DOOR_SPEED)
                self._door_open = False
    

class FireDoor(Doors):
    def __init__(self, door_location):
        self.door_location = door_location
        self.background_location = door_location
        self.frame_location = (door_location[0] - 16, door_location[1] - 32 )
        self.door_image = pygame.image.load("data/door_images/fire_door.png")
        super().__init__()

class WaterDoor(Doors):
    def __init__(self, door_location):
        self.door_location = door_location
        self.background_location = door_location
        self.frame_location = (door_location[0] - 16, door_location[1] - 32 )
        self.door_image = pygame.image.load("data/door_images/water_door.png")
        super().__init__()