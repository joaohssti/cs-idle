import os
import time
import pygame
import config
from scenes.base_scene import BaseScene
from ui.button import Button
from ui.image_button import ImageButton

class IdleScreen(BaseScene):
    def __init__(self, game):
        super().__init__(game)
                
        self.title_font = pygame.font.Font("cs-idle/fonts/Orbitron/orbitron-bold.otf", 20)
        self.timer_font = pygame.font.Font("cs-idle/fonts/Orbitron/orbitron-light.otf", 18)
        self.buttons = []

    def handle_events(self, events):
        super().handle_events(events)
        for event in events:
            for button in self.buttons:
                button.handle_event(event)

    def update(self):
        
        dt = self.game.clock.tick(config.FPS)

        playtime = self.game.save_data.get('playtime', 0.0)
        playtime += dt
        self.game.save_data['playtime'] = playtime

    def draw(self, screen):
        super().draw(screen)

        self.title_text = f"Save carregado: {self.game.current_save}"
        self.title_surf = self.title_font.render(self.title_text,True, config.COR_BUTTON_TEXT)
        self.title_rect = self.title_surf.get_rect(center=(config.LAGRUGA_SCREEN//2, 200))

        screen.blit(self.title_surf, self.title_rect)

        for button in self.buttons:
            button.draw(screen)

        
        playtime = self.game.save_data.get('playtime', 0.0)
        timer_text = f"Tempo Jogado: {int(playtime)}s"
        timer_surf = self.timer_font.render(timer_text, True, config.COR_BUTTON_TEXT)
        timer_rect = timer_surf.get_rect(center=(config.LAGRUGA_SCREEN // 2, 240))
        screen.blit(timer_surf, timer_rect)

