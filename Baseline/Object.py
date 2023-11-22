import pygame

pygame.init()


class Object:
    def __init__(self, x, y, image, scale, surface):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.surface = surface

    def process(self):
        self.update()
        self.surface.blit(self.image, (self.rect.x, self.rect.y))

    def update(self):
        pass
