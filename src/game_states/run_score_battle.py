import time

import pygame

import src.app_config as cfg
from src.enums import Play
from src.controls import ARROW, WSAD
from src.game_states.game_over import GameOver
from src.game_states.play_state import PlayState
from src.game_states.pause import Pause
from src.snake import Snake
import src.ui.ui_elements as ui
from src.utils import get_rand_coord, align_center_to_grid


class RunScoreBattle(PlayState):

    def __init__(self, game, level_config):
        super().__init__(game, level_config)

    def update(self):

        if self.commands[Play.PAUSE] == True:
            self.game.push_game_state(Pause(self.game))
        if self.commands[Play.QUIT] == True:
            self.game.reset_game()
            return

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

        self.reset_command_flags()

    def draw(self, window):
        ui.draw_border(window, self.border, self.level_config.cell_size)
        
        score_surf, score_rect = ui.create_2player_score_banner(
            self.snakes[0].score, self.snakes[1].score
        )
        window.blit(score_surf, score_rect)

        for fruit in self.fruits:
            pygame.draw.rect(
                window, cfg.GREEN, ((fruit), (self.game.display_size)), border_radius=cfg.BORDER_RADIUS
            )
        for snake in self.snakes:
            snake.draw(window)

    def setup_snakes(self):
        grid_center = align_center_to_grid(self.game.window_size, self.level_config.cell_size)
        self.snakes = [
            Snake(
                self.game.window_size, 
                [ARROW],
                self.level_config.cell_size, 
                (grid_center[0] * 1.5, grid_center[1]),           
                (0, 1), color=cfg.PINK, initial_speed=self.level_config.start_speed,
                acceleration=self.level_config.acceleration, length=3
            ),
            Snake(
                self.game.window_size, 
                [WSAD],
                self.level_config.cell_size, 
                (grid_center[0] * .5, grid_center[1]),
                (0, -1), color=cfg.PURPLE, initial_speed=self.level_config.start_speed,
                acceleration = self.level_config.acceleration, length=3
            )
        ]

        for snake in self.snakes:
            snake.moving = True

    def handle_fruit_collision(self, snake):
        for fruit in self.fruits:
            if fruit == snake.head_position:
                snake.eat(self.level_config.growth_rate)
                snake.score += (len(snake.body) * 10)
                self.fruits.remove(fruit)
                self.add_fruit()
