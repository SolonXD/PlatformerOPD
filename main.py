import pygame
from pygame import *
from settings import *
from button import *
from about_us import *
from choose_level_menu import *

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
main_menu_background = pygame.image.load("assets/main_menu_background/main_menu_background.png")
pygame.display.set_icon(pygame.image.load("icon.ico"))

start_button_img = pygame.image.load("assets/menu_buttons/start_game_button.png")
start_button = Button(120, 200, start_button_img, 1.4, screen, choose_level_menu)
about_button_img = pygame.image.load("assets/menu_buttons/about_us_button.png")
about_button = Button(120, 300, about_button_img, 1.4, screen, about_us)
quit_button_img = pygame.image.load("assets/menu_buttons/quit_button.png")
exit_button = Button(120, 400, quit_button_img, 1.4, screen, pygame.QUIT)


def main():
    pygame.display.set_caption("Paper Thief")
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
