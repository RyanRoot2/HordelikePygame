from utils.base_sprite import BaseSprite
from constants import *

class Consecration:
    dynamic_layering = True
    layer = EFFECTS
    count = 0
    # what does type(self) do?
    def __init__(self, pos, *groups):
        
        self.name = "Consecration"
        self.pos = pos
        self.sprite = BaseSprite(self.pos, "assets/consecration.png", type(self).dynamic_layering, type(self).layer, *groups)
        
        print(f"{self.name} cast at position {pos}")