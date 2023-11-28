from settings import *
from button import *
from text import *

pygame.init()


def about_us():
    pygame.display.set_caption("Game")
    pygame.display.flip()
    screen2 = pygame.display.set_mode((WIDTH, HEIGHT))
    about_us_background = pygame.image.load("assets/about_us_background/about_us_background.jpg")
    start_img = pygame.image.load("assets/menu_buttons/MenuButton.png")
    go_back_button = Button(50, 500, start_img, 0.1, screen2, lambda: ())
    ugreninov = Text(200, 100, screen2, "Arial", 36)
    ugreninov.set_text("Артем Угренинов - Тимлид", (255, 255, 255))
    nikylina = Text(200, 200, screen2, "Arial", 36)
    nikylina.set_text("Жанна Никулина - Главный дизайнер", (255, 255, 255))
    alieva = Text(200, 300, screen2, "Arial", 36)
    alieva.set_text("Севинч Алиева - Левел дизайнер", (255, 255, 255))
    korobova = Text(200, 400, screen2, "Arial", 36)
    korobova.set_text("Анна Коробова - Дизайнер механик", (255, 255, 255))
    running = True
    while running:
        screen2.blit(about_us_background, (0, 0))
        go_back_button.process()
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
                pygame.quit()
            go_back_button.update_button(e)
        ugreninov.draw_text()
        nikylina.draw_text()
        alieva.draw_text()
        korobova.draw_text()

        pygame.display.update()
        if go_back_button.clicked:
            running = False
