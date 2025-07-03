from dataclasses import dataclass

import pygame

@dataclass
class SnakeMoveControls:
    up: int
    down: int
    left: int
    right: int


ARROW = SnakeMoveControls(pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT)
WSAD = SnakeMoveControls(pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d)