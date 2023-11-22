from Baseline.Object import *

pygame.init()


class Button(Object):
    def __init__(self, x, y, image, scale, surface, onClickFunction):
        super().__init__(x, y, image, scale, surface)
        self.clicked = False
        self.onClickFunction = onClickFunction
        self.existRightNow = True

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked and self.existRightNow:
                self.clicked = True
                self.onClickFunction()
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
