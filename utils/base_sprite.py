import pygame
from constants import *

class BaseSprite(pygame.sprite.Sprite):
    def __init__(self, pos, image_path, dynamic_layering=False, layer=BACKGROUND, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(center=pos)
        self.dynamic_layering = dynamic_layering
        self._layer = layer

    def update_position(self, new_pos):
        self.rect.center = new_pos # type: ignore
