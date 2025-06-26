from dataclasses import dataclass


@dataclass(frozen=True)
class LevelConfig:
    has_border: bool
    speed: int
    acceleration: float
    cell_size: int
    fruit_qty: int
    growth_rate: int

CLASSIC = LevelConfig(
    has_border=True, 
    speed=6, 
    acceleration=0, 
    cell_size=40,
    fruit_qty=1,
    growth_rate=1
)

BIG = LevelConfig(
    has_border=True, 
    speed=6, 
    acceleration=1.5, 
    cell_size=80, 
    fruit_qty=1,
    growth_rate=1
)

SUPER = LevelConfig(
    has_border=True, 
    speed=8, 
    acceleration=1.5, 
    cell_size=40, 
    fruit_qty=5,
    growth_rate=2
)

EXTREME = LevelConfig(
    has_border=True, 
    speed=10, 
    acceleration=2, 
    cell_size=20, 
    fruit_qty=25,
    growth_rate=5
)

INSANE = LevelConfig(
    has_border=False, 
    speed=12, 
    acceleration=3, 
    cell_size=10, 
    fruit_qty=150,
    growth_rate=15
)

def create_level_config(
    has_border=True,
    speed=6,
    acceleration=0,
    cell_size=40,
    fruit_qty=1,
    growth_rate=1      
):
    return LevelConfig(
        has_border=has_border,
        speed=speed,
        acceleration=acceleration,
        cell_size=cell_size,
        fruit_qty=fruit_qty,
        growth_rate=growth_rate
    )