import pygame
import config
from scenes.base_scene import BaseScene
from ui.button import Button
from ui.image_button import ImageButton

class AboutScene(BaseScene):
    def __init__(self, game):
        super().__init__(game)

        self.title_text = "Criado por João Henrique"
        self.title_font = pygame.font.Font("cs-idle/fonts/Orbitron/orbitron-bold.otf", 50)
        self.title_surf = self.title_font.render(self.title_text,True, config.COR_BUTTON_TEXT)
        self.title_rect = self.title_surf.get_rect(center=(config.LAGRUGA_SCREEN//2, 200))

    def handle_events(self, events):
        super().handle_events(events)
        
    def update(self):
        pass

    def draw(self, screen):
        
        screen.blit(self.title_surf, self.title_rect)

        super().draw(screen)

        