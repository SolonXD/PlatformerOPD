import pygame
from support import import_sprite


class Trap(pygame.sprite.Sprite):
    def __init__(self, x, y, directory, scale):
        super().__init__()
        self.image_sprites = import_sprite(directory)
        self.frame_index = 0
        self.animation_delay = 3
        self.image = self.image_sprites[self.frame_index]
        self.image = pygame.transform.scale(self.image, (scale, scale))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(x, y))

    def animate(self):
        sprites = self.image_sprites
        sprite_index = (self.frame_index // self.animation_delay) % len(sprites)
        self.image = sprites[sprite_index]
        self.frame_index += 1
        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)
        if self.frame_index // self.animation_delay > len(sprites):
            self.frame_index = 0

    def update(self, x_shift):
        self.animate()
        self.rect.x += x_shift

