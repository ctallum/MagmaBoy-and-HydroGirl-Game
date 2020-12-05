import sys
import pygame
from pygame.locals import *

class Game:
    def __init__(self):
        # create pygame window
        WINDOW_SIZE = (640, 480)
        self.screen = pygame.display.set_mode(WINDOW_SIZE, pygame.RESIZABLE)
        pygame.display.set_caption("Magma Boy and Hydro Girl")


    def draw_board(self, board):
        """
        Refresh and draw the game screen
        """
        new_window_size, center_cords = self.adjust_scale()
        # scale internal display to match window
        game_disp = pygame.transform.scale(board.get_board(), new_window_size)
        self.screen.blit(game_disp, center_cords)
        pygame.display.update()

    def adjust_scale(self):
        """
        Adjust internal screen for window scaling

        If the window size is changed, scale the game to the maximum amount
        while keeping the same aspect ratio. Also keep the game centered in the
        window.

        Returns:
            display_size::tuple (height, width)
                The updated height and width of the internal game display
            cords::tuple (x_cord, y_cord)
                The cordinates of the upper left corner of the internal game
                display so that when it is blit onto window, it is centered.
        """
        window_size = self.screen.get_size()

        # if window is longer than aspect ratio
        if window_size[0] / window_size[1] >= 1.5:
            display_size = (int(1.5 * window_size[1]), window_size[1])
        # if window is taller than aspect ratio
        else:
            display_size = (window_size[0], int(.75 * window_size[0]))
        # find cords so that display is centered
        cords = ((window_size[0] - display_size[0]) / 2,
                 (window_size[1] - display_size[1]) / 2)

        return display_size, cords

    def move_player(self, board, player):
        collision_types = {
            'top': False,
            'bottom': False,
            'right': False,
            'left': False}
        player.rect.x += player.movement[0]
        hit_list = self.collision_test(player.rect, board.get_solid_blocks())
        for tile in hit_list:
            if player.movement[0] > 0:
                player.rect.right = tile.left
                collision_types['right'] = True
            elif player.movement[0] < 0:
                player.rect.left = tile.right
                collision_types['left'] = True
        player.rect.y += player.movement[1]
        hit_list = self.collision_test(player.rect, board.get_solid_blocks())
        for tile in hit_list:
            if player.movement[1] > 0:
                player.rect.bottom = tile.top
                collision_types['bottom'] = True
            if player.movement[1] < 0:
                player.rect.top = tile.bottom
                collision_types['top'] = True


        if collision_types['bottom']:
            player.y_velocity = 0
            player.air_timer = 0
        else:
            player.air_timer += 1

        if collision_types['top']:
            player.y_velocity = 0

    @staticmethod
    def collision_test(rect, tiles):
        hit_list = []
        for tile in tiles:
            if rect.colliderect(tile):
                hit_list.append(tile)
        return hit_list

    def draw_player(self, board, player):
        board.display.blit(player.image, (player.rect.x, player.rect.y))













        # clock/time
        # Framerate
        # Score
        # Level number
# Def update board
# Def update characters
    # Update character position based on acceleration, speed, current location
# Def kill
# Def game_over
# Def pushes (in-game buttons)
# Def gems

