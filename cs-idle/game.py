import pygame
import config

from scenes.main_menu import MainMenuScene
from scenes.idle_screen import IdleScreen
from scenes.about import AboutScene
from scenes.saves_scene import SavesScene

class Game:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.running = True
        self.saves_are_updated = False
        self.current_save = "New Game"
        self.save_data = {}

        self.scenes = {
            "MAIN_MENU": MainMenuScene(self),
            "GAME": IdleScreen(self),
            "LOAD": SavesScene(self),
            "ABOUT": AboutScene(self),
        }

        self.current_scene = self.scenes["MAIN_MENU"]


    def switch_scene(self, scene_name):
        if scene_name == "QUIT":
            self.running = False
        elif scene_name in self.scenes:
            self.current_scene = self.scenes[scene_name]
    
    def run(self):
        while self.running:
            
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False
            
            self.current_scene.handle_events(events)
            self.current_scene.update()
            self.screen.fill(config.COR_BACKGROUND)
            self.current_scene.draw(self.screen)
            
            pygame.display.flip()

