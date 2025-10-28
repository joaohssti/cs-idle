import pygame
import json
import config

class Game:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.running = True

    def run(self):
        while self.running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False
            
            self.screen.fill(config.COR_BACKGROUND)
            pygame.display.flip()
            self.clock.tick(config.FPS)