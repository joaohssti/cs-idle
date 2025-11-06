import pygame
import config
import json

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
        self.static_data = self._load_static_data()

        self.scenes = {
            "MAIN_MENU": MainMenuScene(self),
            "LOAD": SavesScene(self),
            "ABOUT": AboutScene(self),
        }

        self.current_scene = self.scenes["MAIN_MENU"]


    def switch_scene(self, scene_name):
        if scene_name == "QUIT":
            self.running = False
        elif scene_name in self.scenes:
            self.current_scene = self.scenes[scene_name]

    def start_game(self):
        new_game_scene = IdleScreen(self)
        self.scenes["GAME"] = new_game_scene
        self.current_scene = self.scenes["GAME"]
    
    def _load_static_data(self):
        data = {}
        try:
            with open('cs-idle/data/shop.json', 'r', encoding='utf-8') as f:
                data['shop'] = json.load(f)
            with open('cs-idle/data/upgrade.json', 'r', encoding='utf-8') as f:
                data['upgrades'] = json.load(f)
        except Exception as e:
            print(f"Erro ao carregar dados estáticos: {e}")
            pygame.quit()
            exit()
        return data
    
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

