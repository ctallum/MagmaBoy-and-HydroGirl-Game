import sys
import pygame
from pygame.locals import *

class Game:
    def __init__(self):
        # create external pygame window
        WINDOW_SIZE = (640, 480)
        self.screen = pygame.display.set_mode(WINDOW_SIZE, pygame.RESIZABLE)
        pygame.display.set_caption("Magma Boy and Hydro Girl")

        # create internal pygame window
        CHUNK_SIZE = 16
        DISPLAY_SIZE = (34 * CHUNK_SIZE, 25 * CHUNK_SIZE)
        self.display = pygame.Surface(DISPLAY_SIZE)

        self.load_game_images()

    def load_game_images(self):
        self.death_screen = pygame.image.load('data/death_screen.png')
        self.death_screen.set_colorkey((255, 0, 255))

    def draw_board(self, board):
        """
        Draw the board.

        Iterate through the game map draw each chunk.
        """
        # draw the full background
        self.display.blit(board.board_image["wall"], (0, 0))

        # draw the solid blocks and liquids
        for y, row in enumerate(board.game_map):
            for x, tile in enumerate(row):
                if tile == '100':
                    self.display.blit(
                        board.board_image["floor_100"], (x * 16, y * 16))
                if tile == '111':
                    self.display.blit(
                        board.board_image["floor_111"], (x * 16, y * 16))
                if tile == '112':
                    self.display.blit(
                        board.board_image["floor_112"], (x * 16, y * 16))
                if tile == '113':
                    self.display.blit(
                        board.board_image["floor_113"], (x * 16, y * 16))
                if tile == '114':
                    self.display.blit(
                        board.board_image["floor_114"], (x * 16, y * 16))
                if tile == '121':
                    self.display.blit(
                        board.board_image["floor_121"], (x * 16, y * 16))
                if tile == '122':
                    self.display.blit(
                        board.board_image["floor_122"], (x * 16, y * 16))
                if tile == '123':
                    self.display.blit(
                        board.board_image["floor_123"], (x * 16, y * 16))
                if tile == '124':
                    self.display.blit(
                        board.board_image["floor_124"], (x * 16, y * 16))
                if tile == '2':
                    self.display.blit(
                        board.board_image["lava_image"], (x * 16, y * 16))
                if tile == '3':
                    self.display.blit(
                        board.board_image["water_image"], (x * 16, y * 16))
                if tile == '4':
                    self.display.blit(
                        board.board_image["goo_image"], (x * 16, y * 16))

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

    def draw_player(self, player):
        self.display.blit(player.image, (player.rect.x, player.rect.y))

    def check_for_death(self, board, player):
        if player.killed_with == "lava":
            is_killed = self.collision_test(player.rect, board.get_lava_pools())
        if player.killed_with == "water":
            is_killed = self.collision_test(player.rect, board.get_water_pools())
        is_killed += self.collision_test(player.rect, board.get_goo_pools())
        if is_killed:
            player.is_alive = False

    def death_sequence(self, board, players, controller):
        while True:
            self.display.blit(self.death_screen, (0, 0))
            self.refresh_window()
            if controller.restart_level(pygame.event.get()):
                break
        self.reset_game(players)        


    def reset_game(self, players):
        for player in players:
            player.reset_character()

    def refresh_window(self):
        """
        Refresh and draw the game screen
        """
        new_window_size, center_cords = self.adjust_scale()
        # scale internal display to match window
        game_disp = pygame.transform.scale(self.display, new_window_size)
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

