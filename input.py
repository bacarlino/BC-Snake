from enum import Enum, auto


class Menu(Enum):
    LEFT = auto()
    RIGHT = auto()
    SELECT = auto()

class Play(Enum):
    SNAKE_ONE_UP = auto()
    SNAKE_ONE_DOWN = auto()
    SNAKE_ONE_LEFT = auto()
    SNAKE_ONE_RIGHT = auto()
    SNAKE_TWO_UP = auto()
    SNAKE_TWO_DOWN = auto()
    SNAKE_TWO_LEFT = auto()
    SNAKE_TWO_RIGHT = auto()
    START = auto()
    PAUSE = auto()
