# import built in libraries
import random

# import third party libraries
import pygame

# importing the enemy class
from enemy_class import Enemy

# build enemy
def generate_enemy(screen, player):
    player_position = (player.player_rect.x, player.player_rect.y)
    while True:
        # randomize enemy position
        enemy_x = random.randint(0, screen.get_width())
        enemy_y = random.randint(0, screen.get_height())
        enemy_pos = pygame.Vector2(enemy_x, enemy_y)

        # ensure enemy is not too close to player
        if enemy_pos.distance_to(player_position) > 300:
            break

    return Enemy(enemy_pos, player_position)