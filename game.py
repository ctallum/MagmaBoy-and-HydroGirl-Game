import sys
import pygame
from pygame.locals import *

class Game:
    # Class Meta Functions
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
        """
        Load death and menu screens from local png files.
        """
        self.death_screen = pygame.image.load('data/death_screen.png')
        self.death_screen.set_colorkey((255, 0, 255))
        self.menu_screen = pygame.image.load('data/menu_screen.png')

    def draw_board(self, board):
        """
        Draw the board.

        Args:
            board::board class object
                board class object that contains information on chunk images
                and thier locations
        """
        # draw the full background
        self.display.blit(board.board_image["wall"], (0, 0))

        # draw the solid blocks and liquids
        for y, row in enumerate(board.game_map):
            for x, tile in enumerate(row):
                if tile == '100':
                    self.display.blit(
                        board.board_image["floor_100"], (x * 16, y * 16))
                elif tile == '111':
                    self.display.blit(
                        board.board_image["floor_111"], (x * 16, y * 16))
                elif tile == '112':
                    self.display.blit(
                        board.board_image["floor_112"], (x * 16, y * 16))
                elif tile == '113':
                    self.display.blit(
                        board.board_image["floor_113"], (x * 16, y * 16))
                elif tile == '114':
                    self.display.blit(
                        board.board_image["floor_114"], (x * 16, y * 16))
                elif tile == '121':
                    self.display.blit(
                        board.board_image["floor_121"], (x * 16, y * 16))
                elif tile == '122':
                    self.display.blit(
                        board.board_image["floor_122"], (x * 16, y * 16))
                elif tile == '123':
                    self.display.blit(
                        board.board_image["floor_123"], (x * 16, y * 16))
                elif tile == '124':
                    self.display.blit(
                        board.board_image["floor_124"], (x * 16, y * 16))
                elif tile == '2':
                    self.display.blit(
                        board.board_image["lava_image"], (x * 16, y * 16))
                elif tile == '3':
                    self.display.blit(
                        board.board_image["water_image"], (x * 16, y * 16))
                elif tile == '4':
                    self.display.blit(
                        board.board_image["goo_image"], (x * 16, y * 16))

    def move_player(self, board, gates, players):
        for player in players:
            collision_types = {
                'top': False,
                'bottom': False,
                'right': False,
                'left': False}
            player.rect.x += player.movement[0]
            collide_blocks = board.get_solid_blocks() + gates.get_solid_blocks()
            hit_list = self.collision_test(player.rect, collide_blocks)
            for tile in hit_list:
                if player.movement[0] > 0:
                    player.rect.right = tile.left
                    collision_types['right'] = True
                elif player.movement[0] < 0:
                    player.rect.left = tile.right
                    collision_types['left'] = True
            player.rect.y += player.movement[1]
            hit_list = self.collision_test(player.rect, collide_blocks)
            for tile in hit_list:
                if player.movement[1] > 0:
                    player.rect.bottom = tile.top
                    collision_types['bottom'] = True
                elif player.movement[1] < 0:
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
        """
        Create a list of tiles a pygame rect is colliding with.

        Args:
            rect::pygame.rect
                A pygame rect that may be colliding with other rects.
            tiles::[rect, rect, rect]
                A list of pygame rects. The function checks to see if the
                arguement "rect" colides with any of these "tiles".
        Returns:
            hit_list::list
                A list of all "tiles" that the argument rect is colliding with.
                If an empty list is returned, the rect is not colliding with
                any tile.
        """
        hit_list = []
        for tile in tiles:
            if rect.colliderect(tile):
                hit_list.append(tile)
        return hit_list

    def draw_player(self, players):
        """
        Draw the player.

        If the player is moving right or left, draw the player as facing that
        direction.

        Args:
            player::[player object, player object]
                a list of player objects that contains movement data as well as
                different images, one for each direction it can face.
        """
        for player in players:
            if player.moving_right:
                player_image = player.side_image
            elif player.moving_left:
                player_image = pygame.transform.flip(player.side_image, True, False)
            else:
                player_image = player.image
            player_image.set_colorkey((255, 0, 255))
            self.display.blit(player_image, (player.rect.x, player.rect.y))

    def check_for_death(self, board, players):
        """
        Check to see if player has falen in pool that kills them.

        If a magma type player collides with a water pool, they die. Likewise,
        if a water type player collides with a lava pool, they die. If either
        type of player collides with a goo pool, they die.

        Args:
            board::board class object
                class object with information on board layout
            players::[player object, player object]
                A list of player class objects.
        """
        for player in players:
            if player.type == "water":
                is_killed = self.collision_test(player.rect, board.get_lava_pools())
            if player.type == "magma":
                is_killed = self.collision_test(player.rect, board.get_water_pools())
            is_killed += self.collision_test(player.rect, board.get_goo_pools())
            if is_killed:
                player.is_alive = False

    def death_sequence(self, board, players, controller):
        """
        Display a death screen until the user presses "ENTER" and the game
        restarts.
        """
        while True:
            self.display.blit(self.death_screen, (0, 0))
            self.refresh_window()
            if controller.press_key(pygame.event.get(), K_RETURN):
                break
        self.reset_game(players)

    def loading_screen(self, controller):
        """
        Display a menu screen until the user presses ENTER.
        """
        while True:
            self.display.blit(self.menu_screen, (0, 0))
            self.refresh_window()
            if controller.press_key(pygame.event.get(), K_RETURN):
                break

    def reset_game(self, players):
        """
        Moves all of the playes to the begining location.
        """
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

    def draw_gates(self, gates):
        """
        Draw gates and buttons.
        """
        self.display.blit(gates.gate_image, gates.gate_location)
        gates.gate_image.set_colorkey((255, 0, 255))

        gates.plate_image.set_colorkey((255, 0, 255))
        for location in gates.plate_locations:
            self.display.blit(gates.plate_image, location)

    def check_for_gate_press(self, gates, players):
        """
        Check to see if either player is touching one of the gate buttons.
        """
        plate_collisions = []
        for player in players:
            plate_collisions += self.collision_test(player.rect, gates.get_plates())
        if plate_collisions:
            gates.plate_is_pressed = True
        else:
            gates.plate_is_pressed = False
        gates.try_open_gate()

    def draw_doors(self, doors):
        for door in doors:
            self.display.blit(door.door_background, door.background_location)
            self.display.blit(door.door_image, door.door_location)
            self.display.blit(door.frame_image, door.frame_location)
            door.frame_image.set_colorkey((255, 0, 255))

    def check_for_door_open(self, door, player):
        door_collision = self.collision_test(player.rect, [door.get_door()])
        if door_collision:
            door.player_at_door = True
        else:
            door.player_at_door = False
        door.try_raise_door()

    def check_for_win(self, doors):
        win = False
        for door in doors:
            pass
