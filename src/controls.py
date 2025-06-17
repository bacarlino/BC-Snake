import pygame

from dataclasses import dataclass
from enum import Enum, auto

class Move(Enum):
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()

@dataclass
class MoveControls:
    up: int
    down: int
    left: int
    right: int

ARROW = MoveControls(pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT)
WSAD = MoveControls(pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d)

class MenuInput(Enum):
    LEFT = auto()
    RIGHT = auto()
    SELECT = auto()

class Play(Enum):
    # SNAKE_ONE_UP = auto()
    # SNAKE_ONE_DOWN = auto()
    # SNAKE_ONE_LEFT = auto()
    # SNAKE_ONE_RIGHT = auto()
    # SNAKE_TWO_UP = auto()
    # SNAKE_TWO_DOWN = auto()
    # SNAKE_TWO_LEFT = auto()
    # SNAKE_TWO_RIGHT = auto()
    START = auto()
    PAUSE = auto()
    QUIT = auto()
