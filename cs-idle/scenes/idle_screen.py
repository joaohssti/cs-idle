import json
import os
import time
import pygame
import config
import utils
from scenes.base_scene import BaseScene
from ui.button import Button
from ui.image_button import ImageButton
from ui.progress_bar import ProgressBar

class IdleScreen(BaseScene):
    def __init__(self, game):
        super().__init__(game)

        # Divide a tela em 2 partes, com 1/3 e com 2/3
        self.screen_rect = self.game.screen.get_rect()
        self.left_frame = pygame.Rect(0, 0, self.screen_rect.width // 3, self.screen_rect.height)
        self.right_frame = pygame.Rect(self.left_frame.width, 0, self.screen_rect.width * 2 // 3, self.screen_rect.height)
        
        self.title_font = pygame.font.Font("cs-idle/fonts/Orbitron/orbitron-bold.otf", 20)
        self.base_font = pygame.font.Font("cs-idle/fonts/Orbitron/orbitron-light.otf", 18)
        self.buttons = []

        # Temperatura
        self.temp_bar = ProgressBar(x=self.left_frame.left + 50, y=700, width=self.left_frame.width - 100, height=30, min_value=self.game.save_data["min_temperature"],max_value=self.game.save_data["max_temperature"])
        self.fire = pygame.image.load("cs-idle/assets/parts/fire.png")
        self.fire = pygame.transform.scale(self.fire, (128, 128)).convert_alpha()
        self.fire_rect = self.fire.get_rect(center=self.left_frame.center)

        # Botão de clicar no computador
        self._build_computer()

        # Frames para abas e conteúdo das abas
        self.tab_bar_rect = pygame.Rect(self.right_frame.left, self.right_frame.top, self.right_frame.width, 100)
        self.content_area_rect = pygame.Rect(self.right_frame.left, self.right_frame.bottom, self.right_frame.width, self.right_frame.height-self.tab_bar_rect.height)
        
        # Cria as abas e calcula o posicionamento
        self.tabs = []
        tab_names = ["Upgrades", "Shop", "Status", "Campanha"]
        self.active_tab = tab_names[0]
        for i, name in enumerate(tab_names):
            center_x = self.tab_bar_rect.left + (self.tab_bar_rect.width / (len(tab_names) + 1)) * (i + 1)
            tab = Button(text=name, 
                         center_pos=(center_x, self.tab_bar_rect.centery), 
                         width=130, height=50, 
                         font=self.base_font, 
                         action=self.create_tab_action(name))
            self.tabs.append(tab)

    def _build_computer(self):
        self.is_overheated = False
        self.computer_click_button = ImageButton(
            image=pygame.image.load("cs-idle/assets/parts/motherboard.png").convert_alpha(),
            width=256, height=256,
            center_pos=self.left_frame.center,
            action= self.computer_click,
            outline_thickness=3
        )

    def _buil_left_frame_info(self):
        self.left_frame_info = []

        title_text = f"Save carregado: {self.game.current_save}"
        title_surf = self.title_font.render(title_text,True, config.COR_BUTTON_TEXT)
        title_rect = title_surf.get_rect(center=(self.left_frame.centerx, 150))
        self.left_frame_info.append((title_surf, title_rect))

        points_text = f"{utils.formatDataUnit(self.game.save_data['click_bytes'])}"
        points_surf = self.base_font.render(points_text, True, config.COR_BUTTON_TEXT)
        points_rect = points_surf.get_rect(center=(self.left_frame.centerx, 200))
        self.left_frame_info.append((points_surf, points_rect))

        timer_text = f"Tempo Jogado: {int(self.game.save_data['playtime'])}s"
        timer_surf = self.base_font.render(timer_text, True, config.COR_BUTTON_TEXT)
        timer_rect = timer_surf.get_rect(center=(self.left_frame.centerx, 250))
        self.left_frame_info.append((timer_surf, timer_rect))

        temp_text = f"Temperatura: {(self.game.save_data['temperature']):.1f}ºC /{(self.game.save_data['max_temperature'])}°C"
        temp_surf = self.base_font.render(temp_text, True, config.COR_BUTTON_TEXT)
        temp_rect = temp_surf.get_rect(center=(self.left_frame.centerx, 680))
        self.left_frame_info.append((temp_surf, temp_rect))

    def create_tab_action(self, tab_name):
        def action():self.active_tab = tab_name;print(tab_name)
        return action
    
    def computer_click(self):
        # bloqueia o funcionamento do clique se exceder temperatura máxima
        if self.is_overheated:
            return
        click_power = 5
        self.game.save_data['click_bytes'] += click_power
        self.game.save_data['temperature'] = min( self.game.save_data['temperature'] + click_power, self.game.save_data['max_temperature']+5)

    def handle_events(self, events):
        super().handle_events(events)
        for event in events:
            for button in self.buttons:
                button.handle_event(event)
            
            self.computer_click_button.handle_event(event)

            for tab in self.tabs:
                tab.handle_event(event)
                
    def update(self):
        # Atualiza o tempo de  jogo
        self.game.save_data['playtime'] += self.game.clock.tick(config.FPS)

        # Reduz a temperatura baseada no resfriamento (ainda não implementada melhoria de resfriamento, então 1ºC/s)
        self.game.save_data['temperature'] = max(self.game.save_data['temperature']  - (1 / config.FPS), self.game.save_data['min_temperature'])
        self.temp_bar.set_value(self.game.save_data['temperature'])
        if self.game.save_data['temperature'] >= self.game.save_data['max_temperature']:        # Computador superaqueceu
            self.is_overheated = True
        elif self.game.save_data['temperature'] <= self.game.save_data['recover_temperature']:  # Computador resfriou o bastante
            self.is_overheated = False
            


    def draw(self, screen):
        super().draw(screen)

        for button in self.buttons:
            button.draw(screen)

        self.computer_click_button.draw(screen)

        self._buil_left_frame_info()
        self.temp_bar.draw(screen)
        if self.is_overheated:
            screen.blit(self.fire, self.fire_rect)

        for surface, rect in self.left_frame_info:
            screen.blit(surface, rect)

        for tab in self.tabs:
            tab.draw(screen)

