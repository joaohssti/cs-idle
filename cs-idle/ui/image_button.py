import pygame
import config # Seu arquivo de configurações (para config.COR_BUTTON_HOVER)

class ImageButton:

    def __init__(self, image, width, height, center_pos, action=None, hover_color=None, outline_thickness=2):
        self.action = action
        self.is_hovered = False
        self.outline_thickness = outline_thickness
        
        self.hover_color = hover_color or config.COR_BUTTON_HOVER

        # Redimensiona a imagem e garante que ela tenha um canal alfa
        self.image = pygame.transform.scale(image, (width, height)).convert_alpha()

        self.rect = self.image.get_rect(center=center_pos)

        # Cria a MÁSCARA para detecção de colisão pixel-perfect
        self.mask = pygame.mask.from_surface(self.image)

        # Pré-renderiza a superfície do contorno (a "silhueta")
        self.outline_surf = self.mask.to_surface(
            setcolor=self.hover_color, 
            unsetcolor=(0, 0, 0, 0) # Torna o fundo transparente
        )

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.is_hovered = False
            
            if self.rect.collidepoint(event.pos):
                # Verificação precisa (pixel-perfect)
                # Converte a posição do mouse para coordenadas locais do botão
                local_pos = (event.pos[0] - self.rect.x, event.pos[1] - self.rect.y)
                
                # Verifica se o pixel na máscara é opaco (valor 1)
                try:
                    if self.mask.get_at(local_pos):
                        self.is_hovered = True
                except IndexError:
                    pass

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # A verificação self.is_hovered é pixel-perfect
            if event.button == 1 and self.is_hovered:
                if self.action:
                    self.action()

    def draw(self, screen):
        
        if self.is_hovered:
            t = self.outline_thickness
            pos = self.rect.topleft
            
            # Lista de deslocamentos (offsets) para as 8 direções
            offsets = [
                (pos[0] - t, pos[1] - t), (pos[0], pos[1] - t), (pos[0] + t, pos[1] - t),
                (pos[0] - t, pos[1]),     (pos[0] + t, pos[1]),
                (pos[0] - t, pos[1] + t), (pos[0], pos[1] + t), (pos[0] + t, pos[1] + t)
            ]
            
            # Blit a silhueta em todas as 8 posições
            # (Use BLEND_RGBA_ADD para um efeito mais brilhante se as cores se sobreporem)
            for offset in offsets:
                screen.blit(self.outline_surf, offset, special_flags=pygame.BLEND_RGBA_MAX) 

        screen.blit(self.image, self.rect)