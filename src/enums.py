from enum import Enum, IntEnum, StrEnum, auto


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


class MenuType(Enum):
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


class LvlAttrEnum(StrEnum):
    HAS_BORDER = "has_border"
    CELL_SIZE = "cell_size"
    START_SPEED = "start_speed"
    ACCELERATION = "acceleration"
    FRUIT_QTY = "fruit_qty"
    GROWTH_RATE = "growth_rate"
    BORDER_COLOR = "border_color"


class SnakeID(Enum):
    ONE = auto()
    TWO = auto()