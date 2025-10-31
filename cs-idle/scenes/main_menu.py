import pygame
import config
from scenes.base_scene import BaseScene
from ui.button import Button

class MainMenuScene(BaseScene):
    def __init__(self, game):
        super().__init__(game)
        
        self.title_text = "Computador Clicker"
        self.title_font = pygame.font.Font("cs-idle/fonts/Orbitron/orbitron-bold.otf", 100)
        self.title_surf = self.title_font.render(self.title_text,True, config.COR_BUTTON_TEXT)
        self.title_rect = self.title_surf.get_rect(center=(config.LAGRUGA_SCREEN//2, 200))
        
        self.buttons = []
        actions = [
            lambda: self.game.switch_scene("GAME"),
            lambda: self.game.switch_scene("LOAD"),
            lambda: self.game.switch_scene("ABOUT"),
            lambda: self.game.switch_scene("QUIT"),
        ]

        button_texts = ["Novo Jogo", "Carregar Jogo", "Sobre o Jogo", "Sair"]
        n_buttons = len(button_texts)

        for i, text in enumerate(button_texts):
            # Calcula posição do botão
            center_pos = (config.LAGRUGA_SCREEN//2, 300+100*i)

            # Cria e adiciona um botão
            button = Button(
                text = text,
                width=350, height=60,
                center_pos=center_pos,
                font=pygame.font.Font("cs-idle/fonts/Orbitron/orbitron-black.otf", 40),
                action=actions[i]
            )
            self.buttons.append(button)

    def handle_events(self, events):
        for event in events:
            for button in self.buttons:
                button.handle_event(event)

    def update(self):
        pass

    def draw(self, screen):

        screen.blit(self.title_surf, self.title_rect)

        for button in self.buttons:
            button.draw(screen)

        