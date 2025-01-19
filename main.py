# import standard libraries
import random
import time
import json

# import third-party libraries
import pygame

# import enemy stuff
import enemy_functions

# import player stuff
import player_functions

# import other pages
from start_screen import start_screen
from game_over_screen import game_over_screen

def main():
    start_time = time.time()
    dt = 0
    enemy_list = []

    # getting level setup
    with open("level_info.json", "r") as file:
        level_setup = json.load(file)

    level_index = 0
    enemy_generation_prob = level_setup[list(level_setup.keys())[level_index]]["enemy_probability"]

    while True:
        # pygame.QUIT event means the user clicked X to close the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        
        # end main game if player loses all of their lives
        if player.num_of_lives <= 0:
            return True
        
        # update elapsed time
        elapsed_time = time.time() - start_time
            
        # player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            player.player_rect.y -= 300 * dt
        if keys[pygame.K_DOWN]:
            player.player_rect.y += 300 * dt
        if keys[pygame.K_LEFT]:
            player.player_rect.x -= 300 * dt
        if keys[pygame.K_RIGHT]:
            player.player_rect.x += 300 * dt

        # window border detection
        if player.player_rect.y < 0:
            player.player_rect.y = 0
        if player.player_rect.y > HEIGHT - player.height:
            player.player_rect.y = HEIGHT - player.height
        if player.player_rect.x < 0:
            player.player_rect.x = 0
        if player.player_rect.x > WIDTH - player.width:
            player.player_rect.x = WIDTH - player.width

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("black")
    
        # level progression based on json file
        if level_index < len(list(level_setup.keys())) - 1:
            if elapsed_time >= level_setup[list(level_setup.keys())[level_index]]["allotted_time"]:
                level_index += 1
                enemy_generation_prob = level_setup[list(level_setup.keys())[level_index]]["enemy_probability"]
                start_time = time.time()
                player.regenerate_lives()

        # generate enemies periodically
        if random.random() < enemy_generation_prob:
            enemy_list.append(enemy_functions.generate_enemy(screen, player))
    
        # update and draw enemies
        for enemy in enemy_list[:]:
            enemy.update(dt) # update enemy position
            if enemy.is_off_screen(WIDTH, HEIGHT):
                enemy_list.remove(enemy) # remove an enemy off enemy_list if they go off screen
            else:
                enemy.draw(screen) # draw generated enemies
            # if enemies collide with player, player loses a life and all enemies disappear
            if enemy.collides_with_player(player.player_rect):
                player.lost_a_life()
                enemy_list.clear()
        
        # draw the player
        player.draw_player(screen)

        # render each player life
        for i, value in enumerate(player.player_lives_list):
            # render text
            text_surface = life_font.render(value, True, "white")
            # blit text onto the screen at different horizontal positions for each value
            screen.blit(text_surface, (25 + i * 40, 25))
    
        # draw the time elapsed as text
        time_text = time_font.render(f"{elapsed_time:.0f}", True, "white")
        time_text_rect = time_text.get_rect(center=(screen.get_width() // 2 , 50))
        screen.blit(time_text, time_text_rect)

        # draw the level the player is on for the first 2 seconds
        if elapsed_time < 2:
            level_text = time_font.render(list(level_setup.keys())[level_index].capitalize(), True, "white")
            level_text_rect = level_text.get_rect(center=(screen.get_width() // 2 , screen.get_height() * .85))
            screen.blit(level_text, level_text_rect)
        

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":

    # screen dimensions
    WIDTH, HEIGHT =  900, 600

    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Dodger Game")
    time_font = pygame.font.SysFont("Arial", 60)
    life_font = pygame.font.SysFont("Arial", 40)
    clock = pygame.time.Clock()
    running = True

    # build player
    player = player_functions.generate_player(screen)

    while True:
        # pygame.QUIT event means the user clicked X to close the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # display start screen
        game_start = start_screen(screen, player)

        if game_start:
            if main(): # main game runs
                restarting = game_over_screen(screen) # show game over screen if player dies
                if not restarting:
                    break
            
            # reset game state
            player.regenerate_lives()
            player = player_functions.generate_player(screen)
        else:
            break

    pygame.quit()