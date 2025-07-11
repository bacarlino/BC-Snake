from src.enums import SnakeID
from src.ui.ui_config import PINK, PURPLE
from src.controls import ARROW, WSAD
from src.snake import Snake
from src.utils import align_center_to_grid


def create_one_player_snakes(window_size, level_config):
    grid_center = align_center_to_grid(window_size, level_config.cell_size)
    return [Snake(
        window_size=window_size,
        controls=[WSAD, ARROW],
        id=SnakeID.ONE,
        cell_size=level_config.cell_size,
        position=grid_center,
        color=PINK, 
        initial_speed=level_config.start_speed,
        acceleration=level_config.acceleration
    )]


def create_two_player_snakes(window_size, level_config):
    grid_center = align_center_to_grid(window_size, level_config.cell_size)
    return [
        Snake(
            window_size=window_size, 
            controls=[ARROW],
            id=SnakeID.ONE,
            cell_size=level_config.cell_size, 
            position=(grid_center[0] * 1.5, grid_center[1]),           
            direction=(0, 1),
            color=PINK, 
            initial_speed=level_config.start_speed,
            acceleration=level_config.acceleration, 
            length=3
        ),
        Snake(
            window_size=window_size, 
            controls=[WSAD],
            id=SnakeID.TWO,
            cell_size=level_config.cell_size, 
            position=(grid_center[0] * .5, grid_center[1]),
            direction=(0, -1),
            color=PURPLE,
            initial_speed=level_config.start_speed,
            acceleration=level_config.acceleration,
            length=3
        )
    ]