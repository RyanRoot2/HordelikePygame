import pygame
from utils.base_sprite import BaseSprite
from constants import *

class BaseEnemy:
    def __init__(self) -> None:
        self.health = 50
        self.max_health = 50
        self.mana = 0

    def get_player_pos(self):
        return SCREEN_CENTER

class Zombie(BaseEnemy):
    def __init__(self, pos, *groups) -> None:
        super().__init__()
        self.layer = ACTORS
        self.groups = groups
        self.pos = pos
        self.sprite = BaseSprite(self.pos, "assets/zombie.png", False, self.layer, *self.groups)
        self.rect = self.sprite.get_rect()

    def update(self):
        pass

    def draw(self):
        pass
