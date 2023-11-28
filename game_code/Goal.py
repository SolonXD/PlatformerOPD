import pygame


class Goal(pygame.sprite.Sprite):
    def __init__(self, x, y, directory, scale):
        super().__init__()
        self.image = pygame.image.load(directory)
        self.image = pygame.transform.scale(self.image, (scale, scale))
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self, x_shift):
        self.rect.x += x_shift
