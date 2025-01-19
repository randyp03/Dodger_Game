# import built in libraries
import random

# import third party libraries
import pygame

# importing the player class
from player_class import Player

# build enemy
def generate_player(screen):
    player_position = pygame.Vector2((screen.get_width() // 2, screen.get_height() // 2))

    return Player(player_position)