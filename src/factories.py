import src.app_config as cfg
from src.controls import ARROW, WSAD
from src.snake import Snake
from src.utils import align_center_to_grid


def create_one_player_snakes(window_size, level_config):
    grid_center = align_center_to_grid(window_size, level_config.cell_size)
    return [Snake(
        window_size=window_size,
        controls=[WSAD, ARROW],
        cell_size=level_config.cell_size,
        position=grid_center,
        color=cfg.PINK, 
        initial_speed=level_config.start_speed,
        acceleration=level_config.acceleration
    )]


def create_two_player_snakes(window_size, level_config):
    grid_center = align_center_to_grid(window_size, level_config.cell_size)
    return [
        Snake(
            window_size=window_size, 
            controls=[ARROW],
            cell_size=level_config.cell_size, 
            position=(grid_center[0] * 1.5, grid_center[1]),           
            direction=(0, 1),
            color=cfg.PINK, 
            initial_speed=level_config.start_speed,
            acceleration=level_config.acceleration, 
            length=3
        ),
        Snake(
            window_size=window_size, 
            controls=[WSAD],
            cell_size=level_config.cell_size, 
            position=(grid_center[0] * .5, grid_center[1]),
            direction=(0, -1),
            color=cfg.PURPLE,
            initial_speed=level_config.start_speed,
            acceleration=level_config.acceleration,
            length=3
        )
    ]