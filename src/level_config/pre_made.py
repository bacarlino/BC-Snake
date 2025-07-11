from src.level_config.level_config import LevelConfig
from src.ui.ui_config import BLUE, RED, WHITE, LT_BLUE


CLASSIC = LevelConfig(
    has_border=True, 
    start_speed=5, 
    acceleration=0, 
    cell_size=40,
    fruit_qty=1,
    growth_rate=1,
    border_color=BLUE   
)

BIG = LevelConfig(
    has_border=True, 
    start_speed=5, 
    acceleration=1.125, 
    cell_size=80, 
    fruit_qty=1,
    growth_rate=1,
    border_color=BLUE
)

SUPER = LevelConfig(
    has_border=True, 
    start_speed=6, 
    acceleration=1.4, 
    cell_size=40, 
    fruit_qty=3,
    growth_rate=2,
    border_color=BLUE
)

EXTREME = LevelConfig(
    has_border=True, 
    start_speed=8, 
    acceleration=1.5, 
    cell_size=20, 
    fruit_qty=8,
    growth_rate=5,
    border_color=RED
)

INSANE = LevelConfig(
    has_border=False, 
    start_speed=10, 
    acceleration=1.75, 
    cell_size=10, 
    fruit_qty=100,
    growth_rate=10,
    border_color=BLUE
)