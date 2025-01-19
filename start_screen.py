# import built in library
import random
import time

# import third-party library
import pygame

# import enemy
import enemy_functions

pygame.init()
screen = pygame.display.set_mode((900, 600))
clock = pygame.time.Clock()
title_font = pygame.font.SysFont("Arial", 60)
text_font = pygame.font.SysFont("Arial", 30)

def start_screen(screen, player, dt=0):
    running = True
    title = "Dodger Game"
    info = "Press Arrow Keys to Avoid Circles"
    texts = ["Start", "Quit"]
    text_rects = []
    enemy_list = []
    start_time = time.time()

    for i, text in enumerate(texts):
        # render text
        text_surface = text_font.render(text, True, "white")
        # create text rect
        text_rect = text_surface.get_rect(center=(screen.get_width() * (i + 1) * .33, screen.get_height() // 2))
        text_rects.append((text, text_surface, text_rect))

    while running:
        # pygame.QUIT event means the user clicked X to close the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                for text,_,rect in text_rects:
                    if rect.collidepoint(pygame.mouse.get_pos()):
                        if text == "Start":
                            return True
                        if text == "Quit":
                            return False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("black")

        # generate enemies periodically
        elasped_time = min(100, int(time.time() - start_time))
        if random.random() < elasped_time * 0.01:
            enemy_list.append(enemy_functions.generate_enemy(screen, player))
        
        # update and draw enemies
        for enemy in enemy_list[:]:
            enemy.update(dt)
            if enemy.is_off_screen(screen.get_width(), screen.get_height()):
                enemy_list.remove(enemy)
            else:
                enemy.draw(screen, "blue")

            if enemy.collides_with_player(player.player_rect):
                enemy_list.remove(enemy)

        # draw the player
        player.draw_player(screen)

        # render the title as text
        title_text = title_font.render(title, True, "white")
        title_text_rect = title_text.get_rect(center=(screen.get_width() // 2 , 125))
        screen.blit(title_text, title_text_rect)

        # render the button texts
        for _, surface, rect in text_rects:
            pygame.draw.rect(screen, "white", rect.inflate(20, 20), width=3)
            screen.blit(surface, rect)
        
        # render the title as text
        info_text = text_font.render(info, True, "white")
        info_text_rect = info_text.get_rect(center=(screen.get_width() // 2 , screen.get_height() * .75))
        screen.blit(info_text, info_text_rect)

        pygame.display.flip()
        dt = clock.tick(60) / 1000
    
    pygame.quit()

if __name__ == "__main__":
    start_screen(screen)