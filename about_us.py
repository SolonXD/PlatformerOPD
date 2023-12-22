from settings import *
from button import *

pygame.init()


def about_us():
    pygame.display.flip()
    screen2 = pygame.display.set_mode((WIDTH, HEIGHT))
    about_us_background = pygame.image.load("assets/about_us_background/about_us_background.png")
    start_img = pygame.image.load("assets/menu_buttons/go_back_button.png")
    go_back_button = Button(50, 500, start_img, 1, screen2, lambda: ())
    running = True
    while running:
        screen2.blit(about_us_background, (0, 0))
        go_back_button.process()
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
                pygame.quit()
            go_back_button.update_button(e)
        pygame.display.update()
        if go_back_button.clicked:
            running = False
