from constants import *
import pygame
import sys
from player.characters.paladin import Paladin
from ui_elements.healthbar import HealthBar
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

player = Paladin((200, 200), groups['actors'], all_sprites)
healthbar = HealthBar(width=200, height=20, color=(0, 255, 0), attached_object=None, border=True, pos=(50, 50))

while True:

    # Game
    screen.fill((100, 100, 100)) 

    # Updates
    input_manager.update()
    player.update()

    player.use_abilities()
    
    # Draws
    all_sprites.draw(screen)
    healthbar.draw(screen, player.health, player.max_health)  # Example health values
    
    pygame.display.flip()  # Update the display
