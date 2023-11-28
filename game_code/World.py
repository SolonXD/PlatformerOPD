import pygame
from settings import *
from Tile import *
from Trap import *
from Player import *
from Goal import *


class World:
    def __init__(self, world_data, screen):
        self.screen = screen
        self.world_data = world_data
        self.world_shift = 0
        self.current_x = 0
        self.gravity = 0.8
        self._setup_world(world_data)

    def _setup_world(self, layout):
        self.tiles = pygame.sprite.Group()
        self.traps = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.goal = pygame.sprite.Group()
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x, y = col_index * tile_size, row_index * tile_size
                if cell == "X":
                    tile = Tile((x, y), tile_size)
                    self.tiles.add(tile)
                elif cell == "t":
                    tile = Trap((x + (tile_size // 4), y + (tile_size // 4)), tile_size // 2)
                    self.traps.add(tile)
                elif cell == "P":
                    player_sprite = Player((x, y))
                    self.player.add(player_sprite)
                elif cell == "G":
                    goal_sprite = Goal((x, y), tile_size)
                    self.goal.add(goal_sprite)