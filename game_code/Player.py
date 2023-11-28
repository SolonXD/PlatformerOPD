import pygame
from support import import_sprite


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.frame_index = 0
        self.animation_speed = 0.15
        self.image = self.animations["idle"][self.frame_index]
        self.rect = self.image.get_rect(topleft=(x, y))
        self.mask = pygame.mask.from_surface(self.image)
        #movement
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 3
        self.jump_move -= 20
        #player status
        self.life = 1
        self.game_over = False
        self.win = False
        self.status = "idle"
        self.facing_right = True
        self.on_ground = False
        self.on_ceiling = False
        self.on_left = False
        self.on_right = False

    def

    def _import_character_assets(self):
        character_path = "assets/player/"
        self.animations = {"idle": [], "walk": [],
                           "jump": [], "fall": [], "lose": [], "win": []}
        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_sprite(full_path)
