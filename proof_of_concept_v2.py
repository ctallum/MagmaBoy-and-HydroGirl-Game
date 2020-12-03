"""
Main file for Magma Boy and Hydro Girl game.
"""

# import pygame and orther needed libraries
import sys
import pygame
from pygame.locals import *

# import classes
from board import Board

def main():
    # inialize the game
    clock = pygame.time.Clock()
    pygame.init()

    # initialize board
    board = Board()
    level = "data/level0.txt" # we can change level design by changing txt file
    board.load_map(level)
    board.load_images()
    board.make_solid_blocks()

    # initialize player
    player_image = pygame.image.load('data/player_images/player.png').convert()
    player_image.set_colorkey((255, 255, 255)) 
    moving_right = False
    moving_left = False
    player_y_momentum = 0
    air_timer = 0
    player_rect = pygame.Rect(0,300, player_image.get_width(), player_image.get_height())

    # main game loop
    while True:
        # draw board 
        board.draw_board()
                
        player_movement = [0, 0]
        if moving_right:
            player_movement[0] += 2.5
        if moving_left:
            player_movement[0] -= 2.5
        player_movement[1] += player_y_momentum
        player_y_momentum += 0.2
        if player_y_momentum > 3:
            player_y_momentum = 3
        
        player_rect, collisions = move(player_rect, player_movement, board.get_solid_blocks())
        
        if collisions['bottom']:
            player_y_momentum = 0
            air_timer = 0
        else:
            air_timer += 1
        
        if collisions['top']:
            player_y_momentum = 0

        board.display.blit(player_image, (player_rect.x, player_rect.y))

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
        board.refresh()
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
