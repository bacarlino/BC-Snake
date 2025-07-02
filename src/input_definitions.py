from dataclasses import dataclass
from enum import Enum, auto

import pygame


class Move(Enum):
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()


class MenuInput(Enum):
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()
    SELECT = auto()
    BACK = auto()


class Play(Enum):
    START = auto()
    PAUSE = auto()
    QUIT = auto()


@dataclass
class MoveControls:
    up: int
    down: int
    left: int
    right: int


ARROW = MoveControls(pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT)
WSAD = MoveControls(pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d)