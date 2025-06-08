import time

import pygame

from .. import config as cfg
from .game_state import GameState
from ..input import Play
from .. import ui_elements as ui


class RunTwoPlayer(GameState):

    def __init__(self, game):
        super().__init__(self, game)

        self.inputs = {
            Play.SNAKE_ONE_UP: False,
            Play.SNAKE_ONE_DOWN: False,
            Play.SNAKE_ONE_LEFT: False,
            Play.SNAKE_ONE_RIGHT: False,
            Play.SNAKE_TWO_UP: False,
            Play.SNAKE_TWO_DOWN: False,
            Play.SNAKE_TWO_LEFT: False,
            Play.SNAKE_TWO_RIGHT: False,
            Play.START: False, 
            Play.PAUSE: False
        }

    def handle_events(self, event):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_UP]:
            self.inputs[Play.SNAKE_ONE_UP] = True
        elif keys[pygame.K_DOWN]:
            self.inputs[Play.SNAKE_ONE_DOWN] = True
        elif keys[pygame.K_LEFT]:
            self.inputs[Play.SNAKE_ONE_LEFT] = True
        elif keys[pygame.K_RIGHT]:
            self.inputs[Play.SNAKE_ONE_RIGHT] = True
        elif keys[pygame.K_w]:
            self.inputs[Play.SNAKE_TWO_UP] = True
        elif keys[pygame.K_s]:
            self.inputs[Play.SNAKE_TWO_DOWN] = True
        elif keys[pygame.K_a]:
            self.inputs[Play.SNAKE_TWO_LEFT] = True
        elif keys[pygame.K_d]:
            self.inputs[Play.SNAKE_TWO_RIGHT] = True

    def update(self):
        time_now = time.perf_counter()
        self.game.snake.update(time_now)
        self.game.update_fruit(self.game.snake)
        self.game.snake.update(time_now)
        self.game.update_fruit(self.game.snake2)

        self.reset_inputs()

    def draw(self, window):
        SCORE_BANNER_SURF, SCORE_BANNER_RECT = ui.create_2player_score_banner(
            self.game.nake.score, self.game.snake2.score
        )
        window.blit(SCORE_BANNER_SURF, SCORE_BANNER_RECT)

        for fruit in self.game.fruits:
            pygame.draw.rect(
                window, cfg.FRUIT_COLOR, ((fruit), (self.display_size))
            )

        for snake in self.game.snakes:
            snake.draw(window)
        
        # self.snake.draw(window)