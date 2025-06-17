import time

import pygame

from src.game_states.game_state import GameState
from src.controls import Play
from src.game_states.start import Start
import src.ui_elements as ui

class MatchOver(GameState):

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
            for snake in self.game.game_state.peek_below().snakes:
                snake.reset()
            self.game.game_state.pop()
            self.game.game_state.push(Start(self.game))
            return
        if self.inputs[Play.QUIT] == True:
            self.game.reset_game()
            return

        time_now = time.perf_counter()
        for snake in self.game.game_state.peek_below().snakes:
            if snake.dead:
                snake.update(time_now)

        self.reset_inputs()

    def draw(self, window):
        self.game.game_state.peek_below().draw(window)
        window.blit(ui.MATCH_OVER_SURF, ui.MATCH_OVER_RECT)

    def reset_snakes(self):
        for snake in self.game.game_state.peek_below().snakes:
            snake.reset()
