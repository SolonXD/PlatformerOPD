from settings import *
from button import *
from levels.level1.level_1 import *
from levels.level2.level_2 import *
from levels.level3.level_3 import *

pygame.init()


def choose_level_menu():
    pygame.display.flip()
    choose_level_menu_background = pygame.image.load("assets/choose_level_menu/choose_level_menu.jpg")
    screen3 = pygame.display.set_mode((WIDTH, HEIGHT))
    start_level1_img = pygame.image.load("assets/choose_level_menu/choose_menu_buttons/button_level_1.png")
    start_level2_img = pygame.image.load("assets/choose_level_menu/choose_menu_buttons/button_level_2.png")
    start_level3_img = pygame.image.load("assets/choose_level_menu/choose_menu_buttons/button_level_3.png")
    go_back_button_img = pygame.image.load("assets/menu_buttons/go_back_button.png")
    go_back_button = Button(50, 500, go_back_button_img, 1, screen3, lambda: ())
    start_level1_button = Button(100, 100, start_level1_img, 1.3, screen3, pre_level_1)
    start_level2_button = Button(100, 200, start_level2_img, 1.3, screen3, pre_level_2)
    start_level3_button = Button(100, 300, start_level3_img, 1.3, screen3, pre_level_3)
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
