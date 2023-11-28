from settings import *
from button import *
from levels.level_1 import *
from levels.level_2 import *
from levels.level_3 import *

pygame.init()


def choose_level_menu():
    pygame.display.flip()
    choose_level_menu_background = pygame.image.load("assets/choose_level_menu/choose_level_menu.jpg")
    screen3 = pygame.display.set_mode((WIDTH, HEIGHT))
    start_img = pygame.image.load("assets/menu_buttons/MenuButton.png")
    go_back_button = Button(50, 500, start_img, 0.1, screen3, lambda: ())
    start_level1_button = Button(430, 100, start_img, 0.1, screen3, level_1)
    start_level2_button = Button(430, 200, start_img, 0.1, screen3, level_2)
    start_level3_button = Button(430, 300, start_img, 0.1, screen3, level_3)
    running = True
    while running:
        screen3.blit(choose_level_menu_background, (0, 0))
        for button in [start_level1_button, start_level2_button, start_level3_button, go_back_button]:
            button.process()
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            for button in [start_level1_button, start_level2_button, start_level3_button, go_back_button]:
                button.update_button(e)
        pygame.display.update()
        if go_back_button.clicked:
            running = False
