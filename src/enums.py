from enum import Enum, auto


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


class MenuTypes(Enum):
    PLAYERS = auto()
    LEVEL = auto()
    MULTIPLAYER = auto()
    CUSTOM = auto()
    BORDER = auto()
    CELL_SIZE = auto()
    START_SPEED = auto()
    ACCELERATION = auto()
    FRUIT_QTY = auto()
    GROWTH_RATE = auto()