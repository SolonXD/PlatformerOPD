import pygame
from settings import *

pygame.init()


def choose_level_menu():
    screen3 = pygame.display.set_mode((WIDTH, HEIGHT))
    running = True
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
                pygame.quit()

    print("i'm clicked")
