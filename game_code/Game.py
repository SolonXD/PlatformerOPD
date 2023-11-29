import pygame
from settings import WIDTH, HEIGHT


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont("impact", 70)
        self.message_color = pygame.Color("red")

    def game_lose(self, player):
        player.game_over = True
        message = self.font.render("You Lose...", True, self.message_color)
        self.screen.blit(message, (WIDTH // 3 + 70, 70))

    def game_win(self, player):
        player.game_over = True
        player.win = True
        message = self.font.render('You Win!!', True, self.message_color)
        self.screen.blit(message, (WIDTH // 3, 70))

    def game_state(self, player, goal):
        if player.life <= 0 or player.rect.y >= HEIGHT:
            self.game_lose(player)
        elif player.rect.colliderect(goal.rect):
            self.game_win(player)
        else:
            None
