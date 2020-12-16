import sys
import pygame
from pygame.locals import *


class Game:
    # game meta functions
    def __init__(self):
        """
        Initialize game.

        Create a public display that the user sees. Also create an internal
        display that only the game handles. The internal will be scaled to
        fit public display.
        """
        # create external pygame window
        WINDOW_SIZE = (640, 480)
        self.screen = pygame.display.set_mode(WINDOW_SIZE, pygame.RESIZABLE)
        pygame.display.set_caption("Magma Boy and Hydro Girl")

        # create internal pygame window
        CHUNK_SIZE = 16
        DISPLAY_SIZE = (34 * CHUNK_SIZE, 25 * CHUNK_SIZE)
        self.display = pygame.Surface(DISPLAY_SIZE)

    def draw_level_screen(self, level_select):
        """
        Draw level selection screen.

        Args:
            level_select::level_select class object
                A class object that contains the images for the level seleciton
                screen.
        """
        # display main level selectio screen background
        self.display.blit(level_select.screen, (0, 0))

        # display the 5 level titles
        for level in range(5):
            # get image from level_select titles dictionary
            image = level_select.titles[level + 1]
            # center title in x direction
            title_x = (self.display.get_width() - image.get_width()) / 2
            # move titles down so that they don't overlap
            title_y = 50 * level + 100
            self.display.blit(image, (title_x, title_y))

        # display the characters on the left and right of level titles
        left_cords = (50, 150)
        right_cords = (430, 150)
        self.display.blit(level_select.left_player, left_cords)
        self.display.blit(level_select.right_player, right_cords)

    def user_select_level(self, level_select, controller):
        """
        Allow for user to select level.

        As user clicks up and down arrows, move level indicator up and down.
        When user clicks <enter>, return which level they selectd.

        Args:
            level_select::level_select class object
                A class object that contains the images for the level seleciton
                screen.
            controller::controler class object
                A contoller object that allows access to keyboard inputs
        """
        # create current level selected index
        level_index = 0
        # create dictionary to map index to level name
        level_dict = {
            0: "level1",
            1: "level2",
            2: "level3",
            3: "level1",
            4: "level1"
        }
        while True:
            # draw the level selection screen
            self.draw_level_screen(level_select)
            # get all pygame inputs
            events = pygame.event.get()
            # if player presses <down>
            if controller.press_key(events, K_DOWN):
                # move index down one
                level_index += 1
                # wrap around if goes past end
                if level_index == 5:
                    level_index = 0
            # if player presses <up>
            if controller.press_key(events, K_UP):
                # move index up one
                level_index -= 1
                # wrap around if goes past end
                if level_index == -1:
                    level_index = 4
            # draw indicator around the currently selected level
            self.draw_level_select_indicator(level_select, level_index)

            # if user clicks enter
            if controller.press_key(events, K_RETURN):
                # return the name of the level using dict
                return level_dict[level_index]

    def draw_level_select_indicator(self, level_select, level_index):
        """
        Draw level indicator around currently selected level

        Args:
            level_select::level_select class object
                A class object that contains the images for the level seleciton
                screen.
            level_index::int
                Intiger value between 0 and 4.
        """
        indicator = level_select.indicator_image
        # center indicator at the center of screen
        location_x = (self.display.get_width() - indicator.get_width()) / 2
        # move indicator down depending on level index
        location_y = level_index * 50 + 96
        # create tuple of cordinates
        indicator_location = (location_x, location_y)
        # draw indicator
        self.display.blit(level_select.indicator_image, indicator_location)
        self.refresh_window()

    def refresh_window(self):
        """
        Refresh and draw the game screen
        """
        new_window_size, center_cords = self.adjust_scale()
        # scale internal display to match window)
        new_disp = pygame.transform.scale(self.display, new_window_size)
        self.screen.blit(new_disp, center_cords)
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

    # game mechanics

    def draw_level_background(self, board):
        """
        Draw the background of the level.

        Args:
            board::board class object
                board class object that contains information on chunk images
                and thier locations
        """
        self.display.blit(board.get_background(), (0, 0))

    def draw_board(self, board):
        """
        Draw the board.

        Args:
            board::board class object
                board class object that contains information on chunk images
                and thier locations
        """
        # draw the full background
        board_textures = board.get_board_textures()
        # draw the solid blocks and liquids
        for y, row in enumerate(board.get_game_map()):
            for x, tile in enumerate(row):
                if tile != "0":
                    self.display.blit(
                        board_textures[f"{tile}"], (x * 16, y * 16)
                    )

    def draw_gates(self, gates):
        """
        Draw gates and buttons.

        Args:
            gates::[gate object, ...]
                A list of gate objects with image and location information.
        """
        for gate in gates:
            # dispaly gate
            self.display.blit(gate.gate_image, gate.gate_location)

            for location in gate.plate_locations:
                # display plate location
                self.display.blit(gate.plate_image, location)

    def draw_doors(self, doors):
        """
        Draw doors

        Args:
            doors::[door object, door object]
                A list of door class objects contianing image and locaiton
                information of door, door background, and fame.
        """
        for door in doors:
            # draw door background
            self.display.blit(door.door_background, door.background_location)
            # draw door
            self.display.blit(door.door_image, door.door_location)
            # draw door frame
            self.display.blit(door.frame_image, door.frame_location)

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
                player_image = pygame.transform.flip(
                    player.side_image, True, False)
            else:
                player_image = player.image
            player_image.set_colorkey((255, 0, 255))
            self.display.blit(player_image, (player.rect.x, player.rect.y))

    def move_player(self, board, gates, players):
        """
        Move player

        This function primarily deals with collisions. The function moves the
        player than checks for collisons with the board and gates. It then
        adjusts the locaiton of the player to account for these collisions.

        Args:
            board::board class object
                board class object that contains information on where solid
                where.
            gates::[gate object, ...]
                A list of gate class objects that contians information on where
                the solid aspects of the gate are.
            players::[player object, player object]
                A list of player objects that contain information on movement
                and position.
        """
        for player in players:
            # For each frame, calculate what it's motion is
            player.calc_movement()
            movement = player.get_movement()

            # create a list of solid blocks
            collide_blocks = board.get_solid_blocks()
            # add solid blocks from each gates
            for gate in gates:
                collide_blocks += gate.get_solid_blocks()

            # create dictionary for which side the player is coliding on
            collision_types = {
                'top': False,
                'bottom': False,
                'right': False,
                'left': False}

            # try movng the player laterally
            player.rect.x += movement[0]
            # get a list of all blocks that the player is colliding with.
            hit_list = self.collision_test(player.rect, collide_blocks)
            for tile in hit_list:
                # if player is moving right
                if movement[0] > 0:
                    # set right side of player to be left side of tile
                    player.rect.right = tile.left
                    collision_types['right'] = True
                # if player is moving left
                elif movement[0] < 0:
                    # set left side of plyaer to be right side of tile
                    player.rect.left = tile.right
                    collision_types['left'] = True

            # try moving the player vertically
            player.rect.y += movement[1]
            # get a list of all blocks that the player is colliding with.
            hit_list = self.collision_test(player.rect, collide_blocks)
            for tile in hit_list:
                # if player is moving down
                if movement[1] > 0:
                    # set bottom of player to top of tile
                    player.rect.bottom = tile.top
                    collision_types['bottom'] = True
                # if player is moving up
                elif movement[1] < 0:
                    # set top of player to bottom of tile
                    player.rect.top = tile.bottom
                    collision_types['top'] = True

            # if player hits ground, lose all y_velocity
            # if player hits ground, reset air_timer
            if collision_types['bottom']:
                player.y_velocity = 0
                player.air_timer = 0
            else:
                player.air_timer += 1

            # if player hit head, lose all y_velocity
            if collision_types['top']:
                player.y_velocity = 0

    def check_for_death(self, board, players):
        """
        Check to see if player has falen in pool that kills them or if they are
        crushed by a gate.

        If a magma type player collides with a water pool, they die. Likewise,
        if a water type player collides with a lava pool, they die. If either
        type of player collides with a goo pool, they die.
        Args:
            board::board class object
                class object with information on board layout
            gates::gate class object
                class object with information on gate location and state
            players::[player object, player object]
                A list of player class objects.
        """
        for player in players:
            # if the player is hydro_girl
            if player.get_type() == "water":
                # see if she collides with lava
                is_killed = self.collision_test(
                    player.rect, board.get_lava_pools())
            # if the player is magma_boy
            if player.get_type() == "magma":
                # see if he collides wit water
                is_killed = self.collision_test(
                    player.rect, board.get_water_pools())
            # see if either collide with goo
            is_killed += self.collision_test(player.rect, board.get_goo_pools())

            # if the is_killed list is longer than 0, kill player
            if is_killed:
                player.kill_player()

    def check_for_gate_press(self, gates, players):
        """
        Check to see if either player is touching one of the gate buttons.

        Args:
            gates::[gate object, ...]
                A list of gate class object containing information on location
                of the gate, the buttons, and images
            players::[player object, player object]
                A list of player class objects containing information on their
                location.
        """
        for gate in gates:
            plate_collisions = []
            for player in players:
                # is player is colliding with plate, add to list
                plates = gate.get_plates()
                plate_collisions += self.collision_test(player.rect, plates)
            # if the collide list is longer than zero, set plate to pressed
            if plate_collisions:
                gate.plate_is_pressed = True
            # otherwise, set plate to not being pressed
            else:
                gate.plate_is_pressed = False
            # attempt to raise the gate. If plate is pressed, gate will raise,
            # otherwise, the gate will close
            gate.try_open_gate()

    def check_for_door_open(self, door, player):
        """
        Check to see if a player is at the door.

        Args:
            door::door class object
                A door object containing information on its locaiton and state
            player::player class object
                A player ojbect containing information on its location
        """
        # check to see if the player is at the door
        door_collision = self.collision_test(player.rect, [door.get_door()])
        # if the collision list is greater than zero, player is at door
        if door_collision:
            door.player_at_door = True
        # otherwise, player is not at door
        else:
            door.player_at_door = False
        # attempt to raise door. If nobody is at door, try to close the door
        door.try_raise_door()

    @staticmethod
    def level_is_done(doors):
        """
        Check to see if the level is complete

        Args:
            doors::[door object, door object]
                A list of door class objects that contain information on their
                state.
        Return:
            is_win::bool
                Return True if level is complete, or False if it is not
        """
        # by default set win to true
        is_win = True
        for door in doors:
            # if either door are not open, set win to False
            if not door.is_door_open():
                is_win = False
        return is_win

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
