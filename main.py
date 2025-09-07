from constants import *
import pygame
from player.characters.paladin import Paladin
from ui_elements.healthbar import HealthBar
from ui_elements.manabar import ManaBar
from common.input_manager import InputManager

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Pygame Window")

groups = {
    'background': pygame.sprite.Group(),
    'terrain': pygame.sprite.Group(),
    'effects': pygame.sprite.Group(),
    'actors': pygame.sprite.Group(),
    'projectiles': pygame.sprite.Group(),
    'ui': pygame.sprite.Group(),
}
all_sprites = pygame.sprite.LayeredUpdates()

input_manager = InputManager()

player = Paladin(SCREEN_CENTER, groups['actors'], all_sprites)
healthbar = HealthBar(width=200, height=20, attached_object=player, border=True, pos=(50, 50))
manabar = ManaBar(width=200, height=20, attached_object=player, border=True, pos=(50, 50))

while True:

    # Game
    screen.fill(CLARET) 

    # Updates
    input_manager.update()
    player.update()

    player.use_abilities()
    
    # Draws
    all_sprites.draw(screen)
    healthbar.draw(screen, player.health, player.max_health)  # Example health values
    manabar.draw(screen, player.health, player.max_health)
    
    pygame.display.flip()  # Update the display
