import pygame
pygame.init()


class Text:
    def __init__(self, x, y, surface, font_name, font_size):
        self.text = None
        self.font = None
        self.x = x
        self.y = y
        self.font_name = font_name
        self.font_size = font_size
        self.surface = surface
        self.set_font()

    def set_font(self):
        self.font = pygame.font.SysFont(self.font_name, self.font_size)

    def set_text(self, text, color):
        self.text = self.font.render(text, True, color)

    def draw_text(self):
        self.surface.blit(self.text, (self.x, self.y))
