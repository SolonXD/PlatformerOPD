import pygame
from settings import *
from game_code.world import World
from button import Button
import time

pygame.init()


def pre_level_2():
    level_2_screen = pygame.display.set_mode((WIDTH, HEIGHT))
    level_2_background = pygame.image.load("assets/level_2/slides/slide_start_1.png")
    level_2_screen.blit(level_2_background, (0, 0))
    pygame.display.update()
    time.sleep(6)
    level_2_background = pygame.image.load("assets/level_2/slides/slide_start_2.png")
    level_2_background = pygame.transform.scale(level_2_background, (WIDTH, HEIGHT))
    level_2_screen.blit(level_2_background, (0, 0))
    pygame.display.update()
    time.sleep(6)
    level_2()


def level_2():
    game_paused = False
    level_2_screen = pygame.display.set_mode((WIDTH, HEIGHT))
    world = World("levels/level2/map.txt", 2, level_2_screen)
    clock = pygame.time.Clock()
    player_event = False
    level_2_background = pygame.image.load("assets/level_2/background/background.jpg")
    level_2_background = pygame.transform.scale(level_2_background, (WIDTH, HEIGHT))
    menu_button_list = list()
    resume_button_img = pygame.image.load("assets/menu_buttons/resume_button.png")
    resume_button = Button(430, 100, resume_button_img, 1.3, level_2_screen, lambda: ())
    menu_button_list.append(resume_button)
    restart_button_img = pygame.image.load("assets/menu_buttons/restart_button.png")
    restart_button = Button(430, 200, restart_button_img, 1.3, level_2_screen, lambda: ())
    menu_button_list.append(restart_button)
    back_to_menu_img = pygame.image.load("assets/menu_buttons/back_to_menu_button.png")
    back_to_menu_button = Button(430, 300, back_to_menu_img, 1.3, level_2_screen, lambda: ())
    menu_button_list.append(back_to_menu_button)
    running = True
    while running:
        level_2_screen.blit(level_2_background, (0, 0))
        if world.game.win:
            time.sleep(2)
            running = False
        if world.game.lose:
            time.sleep(2)
            running = False
            level_2()
        while game_paused:
            # this loop is responsible for the pause menu
            for button in menu_button_list:
                button.process()
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                elif e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        game_paused = not game_paused
                for button in menu_button_list:
                    button.update_button(e)
            if resume_button.clicked:
                game_paused = False
                resume_button.clicked = False
            if restart_button.clicked:
                game_paused = False
                running = False
                level_2()
            if back_to_menu_button.clicked:
                game_paused = False
                running = False
            pygame.display.update()
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    player_event = "space"
                if e.key == pygame.K_LEFT:
                    player_event = "left"
                if e.key == pygame.K_RIGHT:
                    player_event = "right"
                if e.key == pygame.K_ESCAPE:
                    game_paused = not game_paused
            elif e.type == pygame.KEYUP:
                player_event = False
        world.update(player_event)
        pygame.display.update()
        clock.tick(60)
