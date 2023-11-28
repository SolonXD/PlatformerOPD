import pygame
from settings import *

pygame.init()


def level_1():
    level_1_screen = pygame.display.set_mode((WIDTH, HEIGHT))
    running = True
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
                pygame.quit()

