import pygame
import config
from game import Game

def main():

    pygame.init()
    pygame.font.init()

    screen = pygame.display.set_mode((config.LAGRUGA_SCREEN,config.ALTURA_SCREEN))
    pygame.display.set_caption("Idle Computador")

    clock = pygame.time.Clock()

    game = Game(screen, clock)

    game.run()

    pygame.quit()

if __name__ == "__main__":
    main()