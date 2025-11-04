import pygame
import config

class BaseTab:
    """
    Classe base abstrata para todas as abas de conteúdo no painel direito.
    """
    def __init__(self, game):
        self.game = game # Referência ao jogo principal para acessar o save_data

    def handle_event(self, event, content_area):
        """Processa um único evento. 'content_area' é o Rect onde esta aba pode desenhar."""
        pass

    def update(self):
        """Atualiza a lógica da aba (ex: cálculos, animações)."""
        pass

    def draw(self, screen, content_area):
        """Desenha o conteúdo da aba dentro do 'content_area' fornecido."""
        pass

class UpgradeTab(BaseTab):
    def __init__(self, game):
        super().__init__(game)
        
        self.title_font = pygame.font.Font("cs-idle/fonts/Orbitron/orbitron-bold.otf", 20)
        self.upgrades_list = [] 
        
        print("Aba de Upgrades Construída!")
        
    def handle_event(self, event, content_area):
        pass

    def update(self):
        pass

    def draw(self, screen, content_area):
        title_surf = self.title_font.render("Conteúdo da Aba de Upgrades", True, config.COR_BUTTON_TEXT)
        title_rect = title_surf.get_rect(center=content_area.center)
        screen.blit(title_surf, title_rect)


class ShopTab(BaseTab):
    def __init__(self, game):
        super().__init__(game)
        self.title_font = pygame.font.Font("cs-idle/fonts/Orbitron/orbitron-bold.otf", 20)
        self.shop_items = []
        print("Aba de Shop Construída!")

    def handle_event(self, event, content_area):
        pass

    def update(self):
        pass

    def draw(self, screen, content_area):
        title_surf = self.title_font.render("Conteúdo da Aba de Shop", True, config.COR_BUTTON_TEXT)
        title_rect = title_surf.get_rect(center=content_area.center)
        screen.blit(title_surf, title_rect)