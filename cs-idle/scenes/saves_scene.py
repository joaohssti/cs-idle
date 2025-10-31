import os
import json
import pygame
import config
from scenes.base_scene import BaseScene
from scenes.idle_screen import IdleScreen
from ui.button import Button
from ui.image_button import ImageButton

class SavesScene(BaseScene):
    def __init__(self, game):
        super().__init__(game)

        self.buttons = []

        self.title_text = "Selecione seu Jogo"
        self.title_font = pygame.font.Font("cs-idle/fonts/Orbitron/orbitron-bold.otf", 60)
        self.title_surf = self.title_font.render(self.title_text,True, config.COR_BUTTON_TEXT)
        self.title_rect = self.title_surf.get_rect(center=(config.LAGRUGA_SCREEN//2, 200))

        
        
    def load_displayed_saves(self):
        self.saves = self.find_saves()                                              # Encontra os .json da pasta de saves
        self.games = [lambda s=save: self.set_save(s) for save in self.saves]       # cria referência para carregamendo de cada save
        self.deletes = [lambda s=save: self.delete_save(s) for save in self.saves]  # cria referência para remoção de cada save

        self.buttons = []
       
        for i, save in enumerate(self.saves):
            
            # Botão de selecionar o save
            load_save_button = Button(
                text = os.path.splitext(save)[0],       # Remove extensão para exibição
                width=400, height=60,
                center_pos=(config.LAGRUGA_SCREEN//2-300,300+i*100),
                font=pygame.font.Font("cs-idle/fonts/Orbitron/orbitron-light.otf", 20),
                action= self.games[i]
                )
            
            # Botão para excluir o save
            delete_save_button = ImageButton(
                image = pygame.image.load("cs-idle/assets/icons/bin.png").convert_alpha(),
                width=40, height=40,
                center_pos=(config.LAGRUGA_SCREEN//2+300,300+i*100),
                action= self.deletes[i],
                outline_thickness=3
                )
        
            self.buttons.append(load_save_button)
            self.buttons.append(delete_save_button)

    def find_saves(self):
        saves_found = []
        for filename in os.listdir(config.saves_path):
            if filename.endswith('.json'):
                saves_found.append(filename)
        return saves_found
    
    def set_save(self, save):
        self.game.current_save = save
        
        save_path = os.path.join(config.saves_path, save)
        try:
            with open(save_path, 'r') as f:
                self.game.save_data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.game.save_data = {}

        self.game.switch_scene("GAME")

    def delete_save(self, save):
        print(save + " Deleted")

    def handle_events(self, events):
        super().handle_events(events)
        for event in events:
            for button in self.buttons:
                button.handle_event(event)

    def update(self):
        if not self.game.saves_are_updated:
            self.load_displayed_saves()
            self.game.saves_are_updated = True

    def draw(self, screen):
        super().draw(screen)

        screen.blit(self.title_surf, self.title_rect)

        for button in self.buttons:
            button.draw(screen)
