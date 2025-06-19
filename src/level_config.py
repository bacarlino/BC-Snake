from dataclasses import dataclass


@dataclass(frozen=True)
class LevelConfig:
    has_border: bool
    speed: int
    speed_up: float
    cell_size: int
    fruit_qty: int
    growth_rate: int




CLASSIC = LevelConfig(
    has_border=True, 
    speed=6, 
    speed_up=0, 
    cell_size=32, 
    fruit_qty=1,
    growth_rate=1
)

BIG = LevelConfig(
    has_border=True, 
    speed=6, 
    speed_up=1.5, 
    cell_size=64, 
    fruit_qty=1,
    growth_rate=1
)

SUPER = LevelConfig(
    has_border=True, 
    speed=8, 
    speed_up=1.5, 
    cell_size=32, 
    fruit_qty=5,
    growth_rate=2
)

EXTREME = LevelConfig(
    has_border=True, 
    speed=10, 
    speed_up=2, 
    cell_size=16, 
    fruit_qty=25,
    growth_rate=5
)

INSANE = LevelConfig(
    has_border=False, 
    speed=12, 
    speed_up=3, 
    cell_size=8, 
    fruit_qty=150,
    growth_rate=15
)

def create_custom_level(
    has_border=True,
    speed=6,
    speed_up=0,
    cell_size=32,
    fruit_qty=3,
    growth_rate=1      
):
    return LevelConfig(
        has_border=has_border,
        speed=speed,
        speed_up=speed_up,
        cell_size=cell_size,
        fruit_qty=fruit_qty,
        growth_rate=growth_rate
    )