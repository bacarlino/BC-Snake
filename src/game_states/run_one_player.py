import time

import pygame

import src.app_config as cfg
from src.enums import Play
from src.controls import ARROW, WSAD
from src.game_states.play_state import PlayState
from src.snake import Snake
import src.ui.ui_elements as ui
from src.utils import align_center_to_grid


class RunOnePlayer(PlayState):

    def __init__(self, game, level_config):
        super().__init__(game, level_config)
        

    def update(self):

        if self.commands[Play.PAUSE] == True:
            self.game.push_pause()
        if self.commands[Play.QUIT] == True:
            self.game.reset_game()
            return

        time_now = time.perf_counter()
        for snake in self.snakes:
            snake.update(time_now, self.border)

            self.handle_fruit_collision(snake)

            if snake.collision_detected:
                snake.die()
                self.game.push_game_over()

        self.reset_command_flags()

    def draw(self, window):
        if self.level_config.has_border:
            ui.draw_border(window, self.border, self.level_config.cell_size)
        
        score_surf, score_rect = ui.create_score_banner(
            self.snakes[0].score
        )
        window.blit(score_surf, score_rect)
        
        for fruit in self.fruits:
            pygame.draw.rect(
                window, cfg.GREEN, ((fruit), (self.game.display_size)), border_radius=cfg.BORDER_RADIUS
            )
        for snake in self.snakes:
            snake.draw(window)

    def setup_snakes(self):
        self.snakes = [
            Snake(
                self.game.window_size, 
                [WSAD, ARROW],
                self.level_config.cell_size, 
                align_center_to_grid(self.game.window_size, self.level_config.cell_size),           
                color=cfg.PINK, initial_speed=self.level_config.start_speed,
                acceleration=self.level_config.acceleration
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
            
    
