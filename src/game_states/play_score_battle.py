import time

import src.app_config as cfg
from src.controls import ARROW, WSAD
from src.factories import create_two_player_snakes
from src.game_states.game_over import GameOver
from src.game_states.play_state import PlayState
from src.snake import Snake
import src.ui.ui_elements as ui
from src.utils import align_center_to_grid


class PlayScoreBattle(PlayState):

    def __init__(self, game, level_config):
        super().__init__(game, level_config)

    def update_snakes(self):
        time_now = time.perf_counter()
        game_over = False
        
        for snake in self.snakes:
            other_snakes = self.snakes.copy()
            other_snakes.remove(snake)
            snake.update(time_now, self.border, other_snakes)

            self.handle_fruit_collision(snake)

        for snake in self.snakes:
            if snake.collision_detected:
                snake.die()
                game_over = True

        if game_over:
            for snake in self.snakes:
                snake.moving = False
            self.game.push_game_state(GameOver(self.game))

    def draw_score(self, window):
        
        score_surf, score_rect = ui.create_2player_score_banner(
            self.snakes[0].score, self.snakes[1].score
        )
        window.blit(score_surf, score_rect)

    def setup_snakes(self):
        self.snakes = create_two_player_snakes(self.game.window_size, self.level_config)
        for snake in self.snakes:
            snake.moving = True