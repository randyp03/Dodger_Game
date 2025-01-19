# import third party libraries
import pygame

pygame.init()
screen = pygame.display.set_mode((900, 600))
clock = pygame.time.Clock()
title_font = pygame.font.SysFont("Arial", 60)
text_font = pygame.font.SysFont("Arial", 30)

def game_over_screen(screen):
    running = True
    title = "Game Over"
    texts = ["Main Menu", "Quit"]
    text_rects = []

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
                        if text == "Main Menu":
                            return True
                        if text == "Quit":
                            return False
        
        # fill the screen with a color to wipe away anything from last frame
        screen.fill("black")

        # render the title as text
        title_text = title_font.render(title, True, "white")
        title_text_rect = title_text.get_rect(center=(screen.get_width() // 2 , 125))
        screen.blit(title_text, title_text_rect)

        # render the texts
        for _, surface, rect in text_rects:
            pygame.draw.rect(screen, "white", rect.inflate(20, 20), width=3)
            screen.blit(surface, rect)

        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    game_over_screen(screen)