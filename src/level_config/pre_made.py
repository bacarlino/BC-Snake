from src.level_config.level_config import LevelConfig


CLASSIC = LevelConfig(
    has_border=True, 
    start_speed=5, 
    acceleration=0, 
    cell_size=40,
    fruit_qty=1,
    growth_rate=1
)

BIG = LevelConfig(
    has_border=True, 
    start_speed=5, 
    acceleration=1.25, 
    cell_size=80, 
    fruit_qty=1,
    growth_rate=1
)

SUPER = LevelConfig(
    has_border=True, 
    start_speed=6, 
    acceleration=1.25, 
    cell_size=40, 
    fruit_qty=3,
    growth_rate=2
)

EXTREME = LevelConfig(
    has_border=True, 
    start_speed=8, 
    acceleration=2, 
    cell_size=20, 
    fruit_qty=8,
    growth_rate=5
)

INSANE = LevelConfig(
    has_border=False, 
    start_speed=12, 
    acceleration=2.5, 
    cell_size=10, 
    fruit_qty=500,
    growth_rate=20
)