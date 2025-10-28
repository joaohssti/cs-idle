import pygame
import config
from scenes.base_scene import BaseScene
from ui.button import Button

class MainMenuScene(BaseScene):
    def __init__(self, game):
        super().__init__(game)
        
        actions = [
            lambda: self.game.switch_scene("GAME"),
            lambda: self.game.switch_scene("ABOUT"),
            lambda: self.game.switch_scene("QUIT"),
        ]

        self.button = Button(
            text = "about",
            width=100,
            height=50,
            center_pos=(200,200),
            font=pygame.font.Font(None, 50),
            action=lambda: print("about")
        )

    def handle_events(self, events):
        for event in events:
            self.button.handle_event(event)

    def update(self):
        pass

    def draw(self, screen):
        
        self.button.draw(screen)

        