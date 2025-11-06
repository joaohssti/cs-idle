import pygame
import config

class Button:

    def __init__(self, text, width, height, center_pos, font, action=None):
        self.text = text
        self.font = font
        self.action = action

        # cria o retângulo do botão
        self.rect = pygame.Rect(0,0,width, height)
        self.rect.center = center_pos

        # Adiciona as cores
        self.color = config.COR_BUTTON
        self.hover_color = config.COR_BUTTON_HOVER
        self.text_color = config.COR_BUTTON_TEXT

    def handle_event(self, event):
        # Detecta se o mouse está em cima do botão
        if event.type == pygame.MOUSEMOTION:
            self.is_hovered = self.rect.collidepoint(event.pos)

        # Detecta se botão foi clicado e chama ação
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button != 1:
                return
            if not self.rect.collidepoint(event.pos):
                return
            if self.action:
                self.action()


    def draw(self, screen):
        
        is_hovered = self.rect.collidepoint(pygame.mouse.get_pos())
        color  = self.hover_color if is_hovered else self.color

        pygame.draw.rect(screen, color, self.rect, border_radius=10)

        text_surf = self.font.render(self.text,True, self.text_color)
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)

