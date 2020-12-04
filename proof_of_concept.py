"""
Main file for Magma Boy and Hydro Girl game.
"""

# import pygame and orther needed libraries
import sys
import pygame
from pygame.locals import *

def main():
    # inialize the game
    clock = pygame.time.Clock()
    pygame.init()

    # initialize classes
    WINDOW_SIZE = (32 * 25, 24 * 25)
    display = pygame.Surface((32 * 16, 24 * 16))
        # create pygame window
    screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
    pygame.display.set_caption("Magma Boy and Hydro Girl")

    # load images
    player_image = pygame.image.load('data/player_images/player.png').convert()
    player_image.set_colorkey((255, 255, 255))

    wall_image = pygame.image.load('data/board_textures/0.png')
    floor_100 = pygame.image.load('data/board_textures/100.png')
    floor_111 = pygame.image.load('data/board_textures/111.png')
    floor_112 = pygame.image.load('data/board_textures/112.png')
    floor_113 = pygame.image.load('data/board_textures/113.png')
    floor_114 = pygame.image.load('data/board_textures/114.png')
    floor_121 = pygame.image.load('data/board_textures/121.png')
    floor_122 = pygame.image.load('data/board_textures/122.png')
    floor_123 = pygame.image.load('data/board_textures/123.png')
    floor_124 = pygame.image.load('data/board_textures/124.png')
    lava_image = pygame.image.load('data/board_textures/2.png')
    water_image = pygame.image.load('data/board_textures/3.png')
    goo_image = pygame.image.load('data/board_textures/4.png')

    game_map = []

    with open("data/level0.txt") as f:
        for line in f:
            line = line.strip().split(',')  # convert string to list of str
            game_map.append(line)

    moving_right = False
    moving_left = False

    player_y_momentum = 0
    air_timer = 0

    player_rect = pygame.Rect(0,300, player_image.get_width(), player_image.get_height())

    # main game loop
    while True:

        solid_blocks = []
        for y, row in enumerate(game_map):
            for x, tile in enumerate(row):
                if tile == '0':
                    display.blit(wall_image, (x*16, y*16))
                if tile == '100':
                    display.blit(floor_100, (x*16, y*16))
                if tile == '111':
                    display.blit(floor_111, (x*16, y*16))
                if tile == '112':
                    display.blit(floor_112, (x*16, y*16))
                if tile == '113':
                    display.blit(floor_113, (x*16, y*16))
                if tile == '114':
                    display.blit(floor_114, (x*16, y*16))
                if tile == '121':
                    display.blit(floor_121, (x*16, y*16))
                if tile == '122':
                    display.blit(floor_122, (x*16, y*16))
                if tile == '123':
                    display.blit(floor_123, (x*16, y*16))
                if tile == '124':
                    display.blit(floor_124, (x*16, y*16))
                if tile == '2':
                    display.blit(lava_image, (x*16, y*16))
                if tile == '3':
                    display.blit(water_image, (x*16, y*16))
                if tile == '4':
                    display.blit(goo_image, (x*16, y*16))
                if tile not in ['0', '2', '3', '4']:
                    solid_blocks.append(pygame.Rect(x*16, y*16, 16, 16))
                
        player_movement = [0, 0]
        if moving_right:
            player_movement[0] += 2
        if moving_left:
            player_movement[0] -= 2
        player_movement[1] += player_y_momentum
        player_y_momentum += 0.2
        if player_y_momentum > 3:
            player_y_momentum = 3

        player_rect, collisions = move(player_rect, player_movement, solid_blocks)
        
        if collisions['bottom']:
            player_y_momentum = 0
            air_timer = 0
        else:
            air_timer += 1
        
        if collisions['top']:
            player_y_momentum = 0

        display.blit(player_image, (player_rect.x, player_rect.y))

        # check for keyboard input
        for event in pygame.event.get():
            # if player closes the window
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    moving_right = True
                if event.key == K_LEFT:
                    moving_left = True
                if event.key == K_UP:
                    if air_timer < 6:
                        player_y_momentum = -5.5
            if event.type == KEYUP:
                if event.key == K_RIGHT:
                    moving_right = False
                if event.key == K_LEFT:
                    moving_left = False


        # update the diaplay
        surf = pygame.transform.scale(display, WINDOW_SIZE)
        screen.blit(surf, (0,0))
        pygame.display.update()
        # run game at rate of 60 fps
        clock.tick(60)

def collision_test(rect, tiles):
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    return hit_list

def move(rect, movement, tiles):
    collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}
    rect.x += movement[0]
    hit_list = collision_test(rect, tiles)
    for tile in hit_list:
        if movement[0] > 0:
            rect.right = tile.left
            collision_types['right'] = True
        elif movement[0] < 0:
            rect.left = tile.right
            collision_types['left'] = True
    rect.y += movement[1]
    hit_list = collision_test(rect, tiles)
    for tile in hit_list:
        if movement[1] > 0:
            rect.bottom = tile.top
            collision_types['bottom'] = True
        if movement[1] < 0:
            rect.top = tile.bottom
            collision_types['top'] = True
    return rect, collision_types

if __name__ == '__main__':
    main()
