import pygame
from support import import_sprite


class Booster(pygame.sprite.Sprite):
    def __init__(self, x, y, directory, scale, booster_id):
        super().__init__()
        self.image_sprites = import_sprite(directory)
        self.frame_index = 0
        self.animation_delay = 3
        self.image = self.image_sprites[self.frame_index]
        self.scale = scale
        self.image = pygame.transform.scale(self.image, (self.scale, self.scale))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.booster_id = booster_id

    def animate(self):
        sprites = self.image_sprites
        sprite_index = (self.frame_index // self.animation_delay) % len(sprites)
        self.image = sprites[sprite_index]
        self.frame_index += 1
        self.image = pygame.transform.scale(self.image, (self.scale, self.scale))
        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)
        if self.frame_index // self.animation_delay > len(sprites):
            self.frame_index = 0

    def give_buff(self, booster_list):
        if self.booster_id == 1:
            booster_list[self.booster_id - 1] = True
        elif self.booster_id == 2:
            booster_list[self.booster_id - 1] = True
        elif self.booster_id == 3:
            booster_list[self.booster_id - 1] = True
        elif self.booster_id == 4:
            booster_list[self.booster_id - 1] = True
        elif self.booster_id == 5:
            booster_list[self.booster_id - 1] = True

    def update(self, x_shift):
        self.animate()
        self.rect.x += x_shift
