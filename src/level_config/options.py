from dataclasses import dataclass


@dataclass
class LevelAttribute:
    name: str
    value: int | bool


BORDER_ON = LevelAttribute("On", True)
BORDER_OFF = LevelAttribute("Off", False)

CELL_SIZE_TINY = LevelAttribute("Tiny", 10)
CELL_SIZE_SMALL = LevelAttribute("Small", 20)
CELL_SIZE_MEDIUM = LevelAttribute("Medium", 40)
CELL_SIZE_LARGE = LevelAttribute("Large", 80)

START_SPEED_SLOW = LevelAttribute("Slow", 5)
START_SPEED_MEDIUM = LevelAttribute("Medium", 6)
START_SPEED_FAST = LevelAttribute("Fast", 8)

ACCELERATION_NONE = LevelAttribute("None", 0)
ACCELERATION_LOW = LevelAttribute("Low", 1.25)
ACCELERATION_HIGH = LevelAttribute("High", 2)

FRUIT_QTY_LOW = LevelAttribute("Low", 1)
FRUIT_QTY_MEDIUM = LevelAttribute("Medium", 3)
FRUIT_QTY_HIGH = LevelAttribute("High", 8)

GROWTH_RATE_LOW = LevelAttribute("Low", 1)
GROWTH_RATE_MEDIUM = LevelAttribute("Medium", 2)
GROWTH_RATE_HIGH = LevelAttribute("High", 5)

