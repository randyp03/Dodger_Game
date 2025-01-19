import pygame

class Player():
    def __init__(self, spawn_position, speed = 200, color = "red"):
        self.pos = pygame.Vector2(spawn_position) # player position
        self.speed = speed # movement speed (pixels/second)
        self.width, self.height = 40, 40 # player size
        self.color = color
        self.life_symbol = "♥"
        self.num_of_lives = 3
        self.player_lives_list = list(self.life_symbol) * self.num_of_lives

        self.player_rect = pygame.Rect(self.pos.x - self.width / 2 , self.pos.y - self.height / 2, self.width, self.height)

    def draw_player(self, surface):
        # draw the player as a rect
        pygame.draw.rect(surface, self.color, self.player_rect)
    
    def lost_a_life(self):
        self.num_of_lives -= 1
        self.player_lives_list = list(self.life_symbol) * self.num_of_lives
    
    def regenerate_lives(self):
        self.num_of_lives = 3
        self.player_lives_list = list(self.life_symbol) * self.num_of_lives
