import pygame
from settings import *
from game_code.tile import Tile
from Baseline.trap import Trap
from game_code.goal import Goal
from game_code.player import Player
from game_code.game import Game
from game_code.coin_block import CoinBlock
from game_code.score import Score
from game_code.booster import Booster


class World:
    def __init__(self, world_data, level_number, screen):
        self.screen = screen
        self.world_data = None
        self.world_shift = 0
        self.current_x = 0
        self.gravity = 0.5
        self.level_number = level_number
        self.import_map(world_data)
        self.game = Game(self.screen)
        self.score = Score(self.screen, 1)
        self.setup_world(self.world_data)

    def import_map(self, map_directory):
        with open(map_directory) as F:
            game_map = F.read().split("\n")
            self.world_data = game_map

    def setup_world(self, layout):
        self.tiles = pygame.sprite.Group()
        self.coin_blocks = pygame.sprite.Group()
        self.traps = pygame.sprite.Group()
        self.boosters = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.goal = pygame.sprite.GroupSingle()
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x, y = col_index * tile_size, row_index * tile_size
                if cell == "B":
                    tile = Tile(x, y, f"assets/level_{self.level_number}/tile/tile_bottom.png", tile_size)
                    self.tiles.add(tile)
                elif cell == "T":
                    tile = Tile(x, y, f"assets/level_{self.level_number}/tile/tile_top.png", tile_size)
                    self.tiles.add(tile)
                elif cell == "C":
                    tile = CoinBlock(x, y + tile_size // 4, f"assets/level_{self.level_number}/coin_block/coin_block.png", tile_size)
                    self.coin_blocks.add(tile)
                elif cell == "1":
                    tile = Trap(x + tile_size // 4, y + (tile_size // 1.5), f"assets/level_{self.level_number}/traps"
                                                                            f"/trap_id_1/", tile_size // 2, 1)
                    self.traps.add(tile)
                elif cell == "2":
                    tile = Trap(x, y, f"assets/level_{self.level_number}/traps"
                                                                            f"/trap_id_2/", tile_size, 2)
                    self.traps.add(tile)
                elif cell == "v":
                    tile = Booster(x + (tile_size // 4), y + (tile_size // 4), f"assets/level_{self.level_number}/"
                                                                               f"boosters/booster_id_1/", tile_size, 1)
                    self.boosters.add(tile)
                elif cell == "c":
                    tile = Booster(x + (tile_size // 4), y + (tile_size // 4), f"assets/level_{self.level_number}/"
                                                                               f"boosters/booster_id_2/", tile_size, 2)
                    self.boosters.add(tile)
                elif cell == "n":
                    tile = Booster(x + (tile_size // 4), y + (tile_size // 4), f"assets/level_{self.level_number}/"
                                                                               f"boosters/booster_id_4/", tile_size, 4)
                    self.boosters.add(tile)
                elif cell == "m":
                    tile = Booster(x + (tile_size // 4), y + (tile_size // 4), f"assets/level_{self.level_number}/"
                                                                               f"boosters/booster_id_5/", tile_size, 5)
                    self.boosters.add(tile)
                elif cell == "P":
                    player_sprite = Player(x, y, self.level_number)
                    self.player.add(player_sprite)
                elif cell == "G":
                    goal_sprite = Goal(x, y, f"assets/level_{self.level_number}/goal/goal.png", tile_size)
                    self.goal.add(goal_sprite)

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x
        if player_x < WIDTH // 3 and direction_x < 0:
            self.world_shift = 3
            player.speed = 0
        elif player_x > WIDTH - (WIDTH // 3) and direction_x > 0:
            self.world_shift = -3
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 3

    def apply_gravity(self, player):
        player.direction.y += self.gravity
        player.rect.y += player.direction.y

    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                    player.on_left = True
                    self.current_x = player.rect.left
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    player.on_right = True
                    self.current_x = player.rect.right
        if player.on_left and (player.rect.left < self.current_x or player.direction.x >= 0):
            player.on_left = False
        if player.on_right and (player.rect.right > self.current_x or player.direction.x <= 0):
            player.on_right = False

    def vertical_movement_collision(self):
        player = self.player.sprite
        self.apply_gravity(player)
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                # checks if moving towards bottom
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.on_ground = True
                # checks if moving towards up
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    player.on_ceiling = True
        if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
            player.on_ground = False
        if player.on_ceiling and player.direction.y > 0:
            player.on_ceiling = False

    def trap_collision(self):
        player = self.player.sprite
        for sprite in self.traps.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.active_boosters_list[sprite.trap_id - 1] or player.active_boosters_list[3]:
                    player.active_boosters_list[sprite.trap_id - 1] = False
                    player.active_boosters_list[3] = False
                    if player.direction.x < 0 or player.direction.y > 0:
                        player.rect.x += tile_size
                    elif player.direction.x > 0 or player.direction.y > 0:
                        player.rect.x -= tile_size
                else:
                    player.life -= 1

    def coin_block_collision(self):
        player = self.player.sprite
        for i in range(len(self.coin_blocks.sprites())):
            if (self.coin_blocks.sprites()[i].rect.colliderect(player.rect) and self.coin_blocks.sprites()[i].has_coin
                    and not player.on_ground):
                self.score.score += 1
                self.coin_blocks.sprites()[i].has_coin = False

    def booster_collision(self):
        player = self.player.sprite
        for sprite in self.boosters.sprites():
            if sprite.rect.colliderect(player.rect):
                for i in range(len(player.active_boosters_list)):
                    player.active_boosters_list[i] = False
                sprite.give_buff(player.active_boosters_list)
                self.boosters.remove(sprite)

    def update(self, player_event):
        # tiles
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.screen)
        # coin blocks
        self.coin_blocks.update(self.world_shift)
        self.coin_blocks.draw(self.screen)
        # boosters
        self.boosters.update(self.world_shift)
        self.boosters.draw(self.screen)
        # traps
        self.traps.update(self.world_shift)
        self.traps.draw(self.screen)
        # goal
        self.goal.update(self.world_shift)
        self.goal.draw(self.screen)
        # scrolling
        self.scroll_x()
        # player
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.trap_collision()
        self.coin_block_collision()
        self.booster_collision()
        self.player.update(player_event)
        self.player.draw(self.screen)
        # game statistic
        self.score.update(self.player.sprite.active_boosters_list)
        self.game.game_state(self.player.sprite, self.goal.sprite)
