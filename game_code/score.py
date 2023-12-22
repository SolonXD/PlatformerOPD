import pygame
from settings import WIDTH, tile_size


class Score:
    def __init__(self, screen, level_number):
        self.image = None
        self.score_text = None
        self.score = 100
        self.font = pygame.font.SysFont("impact", 50)
        self.message_color = pygame.Color((0, 0, 0))
        self.level_number = level_number
        self.surface = screen

    def draw_booster(self, booster_list):
        if booster_list[0]:
            self.image = pygame.image.load(f"assets/level_{self.level_number}/boosters/booster_id_1/"
                                           f"booster_id_1.png")
        elif booster_list[1]:
            self.image = pygame.image.load(f"assets/level_{self.level_number}/boosters/booster_id_2/booster_id_2.png")
        elif booster_list[2]:
            self.image = pygame.image.load(f"assets/level_{self.level_number}/boosters/booster_id_3/booster_id_3.png")
        elif booster_list[3]:
            self.image = pygame.image.load(f"assets/level_{self.level_number}/boosters/booster_id_4/booster_id_4.png")
        elif booster_list[4]:
            self.image = pygame.image.load(f"assets/level_{self.level_number}/boosters/booster_id_5/booster_id_5.png")
        else:
            return
        self.image = pygame.transform.scale(self.image, (tile_size, tile_size))
        self.surface.blit(self.image, (650, 0))

    def update(self, booster_list):
        self.draw_booster(booster_list)
        self.score_text = self.font.render("СЧЁТ: " + str(self.score), True, self.message_color)
        self.surface.blit(self.score_text, (WIDTH - 200, 0))
