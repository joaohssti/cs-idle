import pygame
import config
from ui.button import Button
import utils

class BaseTab:
    def __init__(self, game):
        self.game = game
        self.static_data = game.static_data
        self.save_data = game.save_data
        self.ui_elements = []
        self.base_font = pygame.font.Font("cs-idle/fonts/Orbitron/orbitron-light.otf", 18)
        self.title_font = pygame.font.Font("cs-idle/fonts/Orbitron/orbitron-bold.otf", 20)

    def handle_event(self, event):
        for element in self.ui_elements:
            element.handle_event(event)

    def update(self):
        pass

    def build_ui(self):
        pass

    def draw(self, screen, content_area):
        for element in self.ui_elements:
            element.draw(screen)

class UpgradeTab(BaseTab):
    def __init__(self, game):
        super().__init__(game)
        self.build_ui()
        print("Aba de Upgrades Construída com Botões!")
    
    # --- Ações de Compra --
    def build_ui(self):
        self.ui_elements = []
        y_offset = 150
        screen_width = self.game.screen.get_rect().width
        center_x = (screen_width // 2) + (screen_width // 4)

        for upgrade_id in self.save_data['unlocked_upgrades']:
            upgrade = self.static_data['upgrades'].get(upgrade_id)

            level = self.save_data['upgrade_levels'].get(upgrade_id, 0)
            max_lvl = upgrade['max_level']
            cost = int(upgrade['base_cost'] * (upgrade['cost_multiplier'] ** level))
            if level < max_lvl:
                text = f"{upgrade['name']} (Nv. {level}/{max_lvl}) - Custo: {utils.formatDataUnit(cost)}"
            else:
                text = f"{upgrade['name']} (Nv. MÁXIMO)"

            button = Button(
                text=text,
                center_pos=(center_x, y_offset),
                width=450,
                height=60,
                font=self.base_font,
                action=self._create_buy_action(upgrade_id)
            )
            self.ui_elements.append(button)
            y_offset += 80

    def _create_buy_action(self, upgrade_id):
        def buy_action():
            upgrade = self.static_data['upgrades'][upgrade_id]
            level = self.save_data['upgrade_levels'].get(upgrade_id, 0)
            if level >= upgrade['max_level']:
                print("nível máximo atingido")
                return
            cost = int(upgrade['base_cost'] * (upgrade['cost_multiplier'] ** level))
            if self.save_data['click_bytes'] < cost:
                print("Sem pontos suficientes")
                return
            
            self.save_data['click_bytes'] -= cost
            self.save_data['upgrade_levels'][upgrade_id] += 1
            
            self.build_ui()
            
        return buy_action

class ShopTab(BaseTab):
    def __init__(self, game):
        super().__init__(game)
        self.build_ui()
        print("Aba de Shop Construída!")

    def build_ui(self):
        self.ui_elements = []

    def handle_event(self, event):
        pass

    def update(self):
        pass

    def draw(self, screen, content_area):
        title_surf = self.title_font.render("Conteúdo da Aba de Shop", True, config.COR_BUTTON_TEXT)
        title_rect = title_surf.get_rect(center=content_area.center)
        screen.blit(title_surf, title_rect)