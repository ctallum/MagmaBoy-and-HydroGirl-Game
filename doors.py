import sys
import pygame
from pygame.locals import *


class Doors:
    def __init__(self):
        # set doors initial height and state
        self.player_at_door = False
        self._height_raised = 0
        self._door_open = False

        self.load_images()
        self.make_rects()

    def load_images(self):
        """
        Load the images for the door
        """
        # load image of door frame and make transparent
        self.frame_image = pygame.image.load("data/door_images/door_frame.png")
        self.frame_image.set_colorkey((255, 0, 255))
        # load image of background
        self.door_background = pygame.image.load(
            "data/door_images/door_background.png")

    def make_rects(self):
        """
        Create pygame rect for the door
        """
        x_cord = self.door_location[0]
        y_cord = self.door_location[1]
        self._rect = pygame.Rect(x_cord, y_cord, self.door_image.get_width(),
                                 self.door_image.get_height())

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
        # set door opening/closing speed
        DOOR_SPEED = 1.5
        door_x = self.door_location[0]
        door_y = self.door_location[1]
        # if there is a player at the door and the door isn't open yet
        if self.player_at_door and not self._door_open:
            # move the door up
            self.door_location = (door_x, door_y - DOOR_SPEED)
            # update internal measure of door height
            self._height_raised += DOOR_SPEED
            # if door has raised 31 pixels
            if self._height_raised >= 31:
                # set door to being fully raised
                self._door_open = True
        # if there is not a player at door and the door as fully open
        elif not self.player_at_door and self._height_raised > 0:
            # move the door down
            self.door_location = (door_x, door_y + DOOR_SPEED)
            # update internal measure of door height
            self._height_raised -= DOOR_SPEED
            # set the door as being not being open
            self._door_open = False


class FireDoor(Doors):
    def __init__(self, door_location):
        CHUNK_SIZE = 16
        # set door loaction as input door loaction
        self.door_location = door_location
        # set door background location as the same as the door
        self.background_location = door_location
        # since the frame is larger than the door, it has to be offset
        self.frame_location = (door_location[0] - CHUNK_SIZE, door_location[1]
                               - 2 * CHUNK_SIZE)
        # load unique door image
        self.door_image = pygame.image.load("data/door_images/fire_door.png")
        super().__init__()


class WaterDoor(Doors):
    def __init__(self, door_location):
        CHUNK_SIZE = 16
        # set door loaction as input door loaction
        self.door_location = door_location
        # set door background location as the same as the door
        self.background_location = door_location
        # since the frame is larger than the door, it has to be offset
        self.frame_location = (door_location[0] - CHUNK_SIZE, door_location[1]
                               - 2 * CHUNK_SIZE)
        # load unique door image
        self.door_image = pygame.image.load("data/door_images/water_door.png")
        super().__init__()
