import json
import os
import time
import pygame
import config
import utils
from scenes.base_scene import BaseScene
from ui.button import Button
from ui.image_button import ImageButton

class IdleScreen(BaseScene):
    def __init__(self, game):
        super().__init__(game)
        
        if self.game.current_save == "New Game":
            with open("cs-idle/data/initial_game_state.json", 'r') as f:
                self.game.save_data = json.load(f)
                print("new game loaded ", self.game.save_data)

        # Divide a tela em 2 partes, com 1/3 e com 2/3
        self.screen_rect = self.game.screen.get_rect()
        self.left_frame = pygame.Rect(0, 0, self.screen_rect.width // 3, self.screen_rect.height)
        self.right_frame = pygame.Rect(self.left_frame.width, 0, self.screen_rect.width * 2 // 3, self.screen_rect.height)
        
        self.title_font = pygame.font.Font("cs-idle/fonts/Orbitron/orbitron-bold.otf", 20)
        self.base_font = pygame.font.Font("cs-idle/fonts/Orbitron/orbitron-light.otf", 18)
        self.buttons = []

        self._build_computer()

    def _build_computer(self):
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

    def computer_click(self):
        click_bytes = self.game.save_data.get('click_bytes', 0.0)
        click_bytes += 1
        self.game.save_data['click_bytes'] = click_bytes
        print(self.game.save_data['click_bytes'])

    def handle_events(self, events):
        super().handle_events(events)
        for event in events:
            for button in self.buttons:
                button.handle_event(event)
            
            self.computer_click_button.handle_event(event)

    def update(self):
        
        dt = self.game.clock.tick(config.FPS)

        playtime = self.game.save_data.get('playtime', 0.0)
        playtime += dt
        self.game.save_data['playtime'] = playtime

    def draw(self, screen):
        super().draw(screen)

        for button in self.buttons:
            button.draw(screen)

        self.computer_click_button.draw(screen)

        self._buil_left_frame_info()

        for surface, rect in self.left_frame_info:
            screen.blit(surface, rect)

