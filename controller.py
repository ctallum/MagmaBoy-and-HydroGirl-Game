import sys
import pygame
from pygame.locals import *


class Controller:
    def __init__(self):
        pass

    def control_player(self, events, player):
        """
        Take keyboard inputs and update player motion variables.

        Args:
            events::list
                list of pygame events
            player::player class object
                A player class object containing movement variables
        """
        for event in events:
            # if a key is pressed down
            if event.type == KEYDOWN:
                # if right key pressed, set character to move right
                if event.key == self._controls["right"]:
                    player.moving_right = True
                # if left key pressed, set character to move left
                elif event.key == self._controls["left"]:
                    player.moving_left = True
                # if up key pressed, set character to jump
                elif event.key == self._controls["up"]:
                    # air_timer allows user to jump slightly after they have
                    # already fallen off of a block, makes game feel more
                    # natural. Common platformer tecnique
                    if player.air_timer < 6:
                        player.jumping = True

            # if the user lifts up on a key
            elif event.type == KEYUP:
                # if no longer pressing right, stop player moving right
                if event.key == self._controls["right"]:
                    player.moving_right = False
                # if no longer pressing left, stop player moving left
                elif event.key == self._controls["left"]:
                    player.moving_left = False
                # if no longer pressing up, stop player from jumping
                elif event.key == self._controls["up"]:
                    player.jumping = False

    @staticmethod
    def press_key(events, key):
        """
        Check if a specific key has been pressed.

        Args:
            events::list
                list of pygame events
            key::pygame event.type name
                name of pygame key
        Returns:
            True if key is pressed, False otherwise
        """
        for event in events:
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == key:
                    return True
        return False


class ArrowsController(Controller):
    # set what keys control what action via dictionary
    def __init__(self):
        self._controls = {
            "left": K_LEFT,
            "right": K_RIGHT,
            "up": K_UP
        }
        super().__init__()


class WASDController(Controller):
    def __init__(self):
        # set what keys control what action via dictionary
        self._controls = {
            "left": K_a,
            "right": K_d,
            "up": K_w
        }
        super().__init__()


class GeneralController(Controller):
    # create a general controller that is not tied to a specific player. This
    # class is used to get user input that is not part of the in-game
    # experience, such as <enter> <escape> and so on.
    pass
