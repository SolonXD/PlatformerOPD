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
        # movement
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 3
        self.jump_move = -20
        # player status
        self.life = 1
        self.game_over = False
        self.win = False
        self.status = "idle"
        self.facing_right = True
        self.on_ground = False
        self.on_ceiling = False
        self.on_left = False
        self.on_right = False

    def animate(self):
        animation = self.animations[self.status]
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0
        image = animation[int(self.frame_index)]
        image = pygame.transform.scale(image, (35, 50))
        if self.facing_right:
            self.image = image
        else:
            flipped_image = pygame.transform.flip(image, True, False)
            self.image = flipped_image
        if self.on_ground and self.on_right:
            self.rect = self.image.get_rect(bottomright=self.rect.bottomright)
        elif self.on_ground and self.on_left:
            self.rect = self.image.get_rect(bottomleft=self.rect.bottomleft)
        elif self.on_ground:
            self.rect = self.image.get_rect(midbottom=self.rect.midbottom)
        elif self.on_ceiling and self.on_right:
            self.rect = self.image.get_rect(topright=self.rect.topright)
        elif self.on_ceiling and self.on_left:
            self.rect = self.image.get_rect(bottomleft=self.rect.topleft)
        elif self.on_ceiling:
            self.rect = self.image.get_rect(midtop=self.rect.midtop)

    def _import_character_assets(self):
        character_path = "assets/player/"
        self.animations = {"idle": [], "walk": [],
                           "jump": [], "fall": [], "lose": [], "win": []}
        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_sprite(full_path)

    def get_move_direction(self, player_event):
        if player_event:
            if player_event == "right":
                self.direction.x = 1
                self.facing_right = True
            elif player_event == "left":
                self.direction.x = -1
                self.facing_right = False
        else:
            self.direction.x = 0

    def jump(self):
        self.direction.y = self.jump_move

