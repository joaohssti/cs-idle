import pygame
from scenes.base_scene import BaseScene
import config

class MainMenuScene(BaseScene):
    def __init__(self, game):
        super().__init__(game)
        
        actions = [
            lambda: self.game.switch_scene("GAME"),
            lambda: self.game.switch_scene("ABOUT"),
            lambda: self.game.switch_scene("QUIT"),
        ]

    def handle_events(self, events):
        pass

    def update(self):
        pass

    def draw(self, screen):
        
        pygame.draw.circle(screen, (0,128,0),(200,200),100)

        