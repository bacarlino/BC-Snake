import time

import pygame

import src.app_config as cfg
from src.enums import Play
from src.controls import ARROW, WSAD
from src.factories import create_two_player_snakes
from src.game_states.play_state import PlayState
from src.game_states.pause import Pause
from src.snake import Snake
import src.ui.ui_elements as ui
from src.utils import align_center_to_grid


class PlayCoOp(PlayState):

    def __init__(self, game, level_config):
        super().__init__(game, level_config)

    def update_snakes(self):
        time_now = time.perf_counter()
        for snake in self.snakes:
            other_snakes = self.snakes.copy()
            other_snakes.remove(snake)
            snake.update(time_now, self.border, other_snakes)

            if snake.collision_detected:
                snake.die()
            
            self.handle_fruit_collision(snake)

        if all([snake.dead for snake in self.snakes]):
            self.game.push_game_over()

    def draw_score(self, window):
        score_surf, score_rect = ui.create_score_banner(
            self.snakes[0].score + self.snakes[1].score
        )
        window.blit(score_surf, score_rect)

    def setup_snakes(self):
        self.snakes = create_two_player_snakes(self.game.window_size, self.level_config)
        for snake in self.snakes:
            snake.moving = True

        for snake in self.snakes:
            snake.moving = True