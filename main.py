import pygame

import config as cfg
from game import Game


def main():
    pygame.init()
    window = pygame.display.set_mode((cfg.WINDOW_W, cfg.WINDOW_H))
    pygame.display.set_caption("BC-Snake")

    game = Game((cfg.WINDOW_W, cfg.WINDOW_H))
    game.run(window)

    pygame.quit()

if __name__ == "__main__":
    main()
