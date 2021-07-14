from typing import Text
import pygame
import sys

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((400,500))
background_colour = (250,250,250)
pygame.display.set_caption('Note')
base_font = pygame.font.Font(None,22)
user_text = ''



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_BACKSPACE:
              user_text = user_text[:-1]
          else:
            user_text += event.unicode


    screen.fill(background_colour)

    text_surface = base_font.render(user_text,True,(0,0,0))
    screen.blit(text_surface,(0,0))

    pygame.display.flip()
    clock.tick(60)


