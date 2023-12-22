import pygame
from support import import_sprite
from settings import player_size_x, player_size_y


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, level_number):
        super().__init__()
        # get player sprite
        self.level_number = level_number
        self._import_character_assets()
        self.frame_index = 0
        self.animation_speed = 0.15
        self.image = self.animations["idle"][self.frame_index]
        self.image = pygame.transform.scale(self.image, (player_size_x, player_size_y))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.mask = pygame.mask.Mask((player_size_x, player_size_y))
        # movement
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 3
        self.jump_move = -15
        # player status
        self.life = 1
        self.has_booster = False
        self.active_boosters_list = [False, False, False, False, False]
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
        image = pygame.transform.scale(image, (player_size_x, player_size_y))
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
        character_path = f"assets/level_{self.level_number}/player/"
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
        if self.active_boosters_list[4]:
            self.direction.y = self.jump_move * 1.3
        else:
            self.direction.y = self.jump_move

    def get_status(self):
        if self.direction.y < 0:
            self.status = "jump"
        elif self.direction.y > 1:
            self.status = "fall"
        elif self.direction.x != 0:
            self.status = "walk"
        else:
            self.status = "idle"

    def update(self, player_event):
        self.get_status()
        if self.life > 0 and not self.game_over:
            if player_event == "space" and self.on_ground:
                self.jump()
            else:
                self.get_move_direction(player_event)
        elif self.game_over and self.win:
            self.direction.x = 0
            self.status = "win"
        else:
            self.direction.x = 0
            self.status = "lose"
        self.animate()
