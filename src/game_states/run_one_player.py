import time

import pygame

import src.config as cfg
from src.input import Play
from src.game_states.game_over import GameOver
from src.game_states.game_state import GameState
from src.game_states.pause import Pause
from src.snake import Snake
import src.ui_elements as ui


class RunOnePlayer(GameState):

    def __init__(self, game):
        super().__init__(game)
        self.game.clear_snakes()
        self.game.add_snake(
            Snake(
                self.game.window_size, self.game.cell_size, 
                (self.game.window_w // 2, self.game.window_h // 2),
                color=cfg.PINK
            )
        )

        self.border = ui.create_border(self.game.cell_size)

        self.inputs = {
            Play.SNAKE_ONE_UP: False,
            Play.SNAKE_ONE_DOWN: False,
            Play.SNAKE_ONE_LEFT: False,
            Play.SNAKE_ONE_RIGHT: False,
            Play.START: False, 
            Play.PAUSE: False,
            Play.QUIT: False
        }

    def handle_events(self, event):

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.inputs[Play.PAUSE] = True
            if event.key == pygame.K_ESCAPE:
                self.inputs[Play.QUIT] = True


        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_UP]:
            self.inputs[Play.SNAKE_ONE_UP] = True
        elif keys[pygame.K_DOWN]:
            self.inputs[Play.SNAKE_ONE_DOWN] = True
        elif keys[pygame.K_LEFT]:
            self.inputs[Play.SNAKE_ONE_LEFT] = True
        elif keys[pygame.K_RIGHT]:
            self.inputs[Play.SNAKE_ONE_RIGHT] = True


    def update(self):

        if self.inputs[Play.PAUSE] == True:
            self.game.change_state(Pause(self.game))
        if self.inputs[Play.QUIT] == True:
            self.game.reset_game()
            return

        time_now = time.perf_counter()

        if self.inputs[Play.SNAKE_ONE_UP]:
            self.game.snakes[0].next_direction = "up"
        if self.inputs[Play.SNAKE_ONE_DOWN]:
            self.game.snakes[0].next_direction = "down"
        if self.inputs[Play.SNAKE_ONE_LEFT]:
            self.game.snakes[0].next_direction = "left"
        if self.inputs[Play.SNAKE_ONE_RIGHT]:
            self.game.snakes[0].next_direction = "right"

        for index, snake in enumerate(self.game.snakes):
            snake.update(time_now, self.border)
            if snake.collide:
                snake.die()
                self.game.change_state(GameOver(self.game))
            self.game.update_fruit(snake, index)

        self.reset_inputs()

    def draw(self, window):
        SCORE_BANNER_SURF, SCORE_BANNER_RECT = ui.create_score_banner(
            self.game.scores[0]
        )
        window.blit(SCORE_BANNER_SURF, SCORE_BANNER_RECT)

        for fruit in self.game.fruits:
            pygame.draw.rect(
                window, cfg.LIME, ((fruit), (self.game.display_size))
            )

        ui.draw_border(window, self.border, self.game.cell_size)
        
        for snake in self.game.snakes:
            snake.draw(window)

        # self.snake.draw(window)
        