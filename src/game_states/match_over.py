import time

import pygame

from src.game_states.game_state import GameState
from src.enums import Play
from src.ui.ui_elements import MatchOverBanner, PressSpaceBanner

class MatchOver(GameState):

    def __init__(self, game):
        super().__init__(game)
        self.match_over_banner = MatchOverBanner()
        self.press_space_banner = PressSpaceBanner()

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
            for snake in self.game.game_state.peek_below().snakes:
                snake.reset()
            self.game.next_round()
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
        self.match_over_banner.draw(window)
        self.press_space_banner.draw(window)

    def reset_snakes(self):
        for snake in self.game.game_state.peek_below().snakes:
            snake.reset()
