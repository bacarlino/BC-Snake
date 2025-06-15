from dataclasses import dataclass

@dataclass
class LevelConfig:
    has_border: bool
    speed: int
    acceleration: float
    cell_size: int
    fruit_qty: int
    growth_rate: int


"""
LevelConfig(
    has_border, speed, acceleration, cell_size, fruit_qty, growth_rate
)
"""
CLASSIC = LevelConfig(
    has_border=True, 
    speed=5, 
    acceleration=0, 
    cell_size=32, 
    fruit_qty=1,
    growth_rate=1
)

BIG = LevelConfig(
    has_border=True, 
    speed=5, 
    acceleration=0, 
    cell_size=64, 
    fruit_qty=1,
    growth_rate=1
)

SUPER = LevelConfig(
    has_border=True, 
    speed=6, 
    acceleration=1.5, 
    cell_size=32, 
    fruit_qty=5,
    growth_rate=2
)

EXTREME = LevelConfig(
    has_border=True, 
    speed=8, 
    acceleration=2.5, 
    cell_size=16, 
    fruit_qty=25,
    growth_rate=5
)
BIG = LevelConfig(True, 6, 0, 64, 1, 1)
super = LevelConfig(True, 6, 1.5, 32, 3, 2)
extreme = LevelConfig(False,6, 2.5, 16, 25, 5)
