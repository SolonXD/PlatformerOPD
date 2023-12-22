import pygame


class Button:
    def __init__(self, x, y, image, scale, surface, onClickFunction):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.surface = surface
        self.clicked = False
        self.onClickFunction = onClickFunction
        self.existRightNow = True

    def update_button(self, event):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.clicked = True
                self.onClickFunction()
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self.clicked = False

    def process(self):
        self.surface.blit(self.image, (self.rect.x, self.rect.y))
