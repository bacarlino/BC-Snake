from dataclasses import dataclass

from src.enums import LvlAttrEnum


@dataclass
class LvlAttrCfg:
    name: str
    value: int | bool
    attr: str


BORDER_ON = LvlAttrCfg("On", True, LvlAttrEnum.HAS_BORDER)
BORDER_OFF = LvlAttrCfg("Off", False, LvlAttrEnum.HAS_BORDER)

CELL_SIZE_TINY = LvlAttrCfg("Tiny", 10, LvlAttrEnum.CELL_SIZE)
CELL_SIZE_SMALL = LvlAttrCfg("Small", 20, LvlAttrEnum.CELL_SIZE)
CELL_SIZE_MEDIUM = LvlAttrCfg("Medium", 40, LvlAttrEnum.CELL_SIZE)
CELL_SIZE_LARGE = LvlAttrCfg("Large", 80, LvlAttrEnum.CELL_SIZE)

START_SPEED_SLOW = LvlAttrCfg("Slow", 5, LvlAttrEnum.START_SPEED)
START_SPEED_MEDIUM = LvlAttrCfg("Medium", 6, LvlAttrEnum.START_SPEED)
START_SPEED_FAST = LvlAttrCfg("Fast", 8, LvlAttrEnum.START_SPEED)

ACCELERATION_NONE = LvlAttrCfg("None", 0, LvlAttrEnum.ACCELERATION)
ACCELERATION_LOW = LvlAttrCfg("Low", 1.25, LvlAttrEnum.ACCELERATION)
ACCELERATION_HIGH = LvlAttrCfg("High", 2, LvlAttrEnum.ACCELERATION)

FRUIT_QTY_LOW = LvlAttrCfg("Low", 1, LvlAttrEnum.FRUIT_QTY)
FRUIT_QTY_MEDIUM = LvlAttrCfg("Medium", 3, LvlAttrEnum.FRUIT_QTY)
FRUIT_QTY_HIGH = LvlAttrCfg("High", 8, LvlAttrEnum.FRUIT_QTY)

GROWTH_RATE_LOW = LvlAttrCfg("Low", 1, LvlAttrEnum.GROWTH_RATE)
GROWTH_RATE_MEDIUM = LvlAttrCfg("Medium", 2, LvlAttrEnum.GROWTH_RATE)
GROWTH_RATE_HIGH = LvlAttrCfg("High", 5, LvlAttrEnum.GROWTH_RATE)

