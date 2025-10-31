import pygame
import json
import os
from datetime import datetime
from ui.image_button import ImageButton
import config
class BaseScene:
    def __init__(self, game):
        self.game = game

        # Botão Power
        self.power_button = ImageButton(
            image = pygame.image.load("cs-idle/assets/icons/power.png").convert_alpha(),
            width=40, height=40,
            center_pos=(50,50),
            action= self.menu_button,
            outline_thickness=3
        )

        # Botão Save
        self.save_button = ImageButton(
            image=pygame.image.load("cs-idle/assets/icons/save.png").convert_alpha(),
            width=40, height=40,
            center_pos=(100, 50),
            action= self.save_button,
            outline_thickness=3
        )
        
        # Botão Volume
        self.volume_button = ImageButton(
            image=pygame.image.load("cs-idle/assets/icons/volume.png").convert_alpha(),
            width=40, height=40,
            center_pos=(150, 50),
            action= lambda: print("VOLUME"),
            outline_thickness=3
        )
        self.common_ui_elements = [self.power_button, self.save_button, self.volume_button]

    def menu_button(self):
        self.game.current_save = "New Game"
        self.game.save_data = {}
        self.game.switch_scene("MAIN_MENU")

    def save_button(self):
        self.game.saves_are_updated = False

        # Dá nome a um save de um novo jogo
        if self.game.current_save == "New Game":
            self.game.current_save =  f"{str(datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))}.json"

        print(self.game.current_save)
        # Salva o estado do jogo
        save_path = os.path.join(config.saves_path, self.game.current_save)
        try:
            with open(save_path, 'w') as f:
                json.dump(self.game.save_data, f, indent=4)
                print("Jogo Salvo")
        except Exception as e:
            print(f"Erro ao salvar o jogo: {e}")

    def handle_events(self, events):
        for event in events:
            for button in self.common_ui_elements:
                button.handle_event(event)
    
    def update(self):
        raise NotImplementedError
    
    def draw(self, screen):
        for element in self.common_ui_elements:
            element.draw(screen)