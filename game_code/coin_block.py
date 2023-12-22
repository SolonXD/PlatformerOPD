import pygame
from game_code.tile import Tile


class CoinBlock(Tile):
    def __init__(self, x, y, directory, scale):
        super().__init__(x, y, directory, scale)
        self.has_coin = True

    def update(self, x_shift):
        self.rect.x += x_shift