import time

import pygame

from src.game_states.game_state import GameState
from src.input import Play
from src.game_states.start import Start
import src.ui_elements as ui

class GameOver(GameState):

    def __init__(self, game):
        super().__init__(game)

        self.inputs = {
            Play.START: False,
            Play.QUIT: False
        }

    def handle_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.inputs[Play.START] = True
            if event.key == pygame.K_ESCAPE:
                self.inputs[Play.QUIT] = True

    def update(self):
        if self.inputs[Play.START] == True:
            self.game.reset_snakes()
            self.game.change_state(Start(self.game))
        if self.inputs[Play.QUIT] == True:
            self.game.reset_game()

        # for snake in self.game.run_state.snake:
            # if self.game.run_state.snake.dead:
        time_now = time.perf_counter()
        self.game.run_state.snake.update(time_now)

        self.reset_inputs()

    def draw(self, window):
        self.game.run_state.draw(window)
        window.blit(ui.GAME_OVER_SURF, ui.GAME_OVER_RECT)