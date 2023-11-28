import pygame
from pygame import *
from settings import *
from button import *
from about_us import *
from choose_level_menu import *

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
main_menu_background = pygame.image.load("assets/main_menu_background/main_menu_background.png")


start_img = pygame.image.load("assets/menu_buttons/MenuButton.png")
start_button = Button(80, 100, start_img, 0.1, screen, choose_level_menu)
about_button = Button(80, 200, start_img, 0.1, screen, about_us)
exit_button = Button(80, 300, start_img, 0.1, screen, pygame.QUIT)

def main():
    pygame.display.set_caption("Game")
    running = True
    while running:
        screen.blit(main_menu_background, (0, 0))
        for button in [start_button, about_button, exit_button]:
            button.process()
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            for button in [start_button, about_button, exit_button]:
                button.update_button(e)
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
