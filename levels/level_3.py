import pygame
from settings import *

pygame.init()

def level_3():
    level_3_screen = pygame.display.set_mode((WIDTH, HEIGHT))
    running = True
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
                pygame.quit()
        level_3_screen.fill((255, 200, 200))
        pygame.display.update()
