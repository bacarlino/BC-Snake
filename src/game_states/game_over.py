import time

import pygame

from src.game_states.game_state import GameState
from src.input import Play
from src.game_states.start import Start
import src.ui_elements as ui

class GameOver(GameState):

    def __init__(self, game):
        super().__init__(game)

        self.commands = {
            Play.START: False,
            Play.QUIT: False
        }

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.commands[Play.START] = True
            if event.key == pygame.K_ESCAPE:
                self.commands[Play.QUIT] = True

    def update(self):
        if self.commands[Play.START] == True:
            self.game.restart_game()
            return
        if self.commands[Play.QUIT] == True:
            self.game.reset_game()
            return

        time_now = time.perf_counter()
        for snake in self.game.game_state.peek_below().snakes:
            if snake.dead:
                snake.update(time_now)

        self.reset_command_flags()

    def draw(self, window):
        # self.game.game_state.peek_below().draw(window)
        window.blit(ui.GAME_OVER_SURF, ui.GAME_OVER_RECT)

    def reset_snakes(self):
        for snake in self.game.game_state.peek_below().snakes:
            snake.reset()
