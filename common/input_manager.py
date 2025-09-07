import pygame
import sys

class InputManager:
    def __init__(self) -> None:
        self.actions = {
            "up": False,
            "down": False,
            "left": False,
            "right": False
        }

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Closing")
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print("Escape pressed")
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.KEYUP:
                pass

if __name__ == "__main__":
    pass
