# ui/bar.py
import pygame
import config

class ProgressBar:
    # Uma classe de UI para exibir uma barra de progresso horizontal.
    def __init__(self, x, y, width, height, min_value, max_value, 
                 color_bg=config.COR_PRIMARY, 
                 color_fill=(255, 80, 80),  # Vermelho para temperatura
                 ):
        
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
        self.min_value = min_value
        self.max_value = max_value
        self.current_value = 0
                
        self.color_bg = color_bg
        self.color_fill = color_fill
        
        self.bg_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.fill_rect = pygame.Rect(self.x, self.y+5, 0, self.height-10)

    def set_value(self, value):
        # Garante que o valor fique entre o mínimo e o máximo
        self.current_value = max(self.min_value, min(value, self.max_value))
        
        # Calcula a largura da barra de preenchimento
        fill_ratio = (self.current_value - self.min_value) / (self.max_value- self.min_value)
        self.fill_rect.width = int(self.width * fill_ratio)

    def draw(self, screen):
        # Desenha o fundo da barra
        pygame.draw.rect(screen, self.color_bg, self.bg_rect, border_radius=5)
        
        # Desenha o preenchimento da barra
        pygame.draw.rect(screen, self.color_fill, self.fill_rect, border_radius=5)