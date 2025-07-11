import time

import pygame

from src.game_states.game_state import GameState
from src.enums import Play
from src.ui.ui_elements import MatchOverBanner, PressSpaceBanner
from src.ui.ui_config import CENTER, COMMAND_BAR_MIDBOTTOM

class MatchOver(GameState):

    def __init__(self, game):
        super().__init__(game)
        self.match_over_banner = MatchOverBanner()
        self.command_bar = PressSpaceBanner()
        self.layout_ui()

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
            self.game.get_previous_state().reset_snakes()
            # for snake in self.game.get_previous_state():
            #     snake.reset()
            self.game.next_round()
            return
        if self.commands[Play.QUIT] == True:
            self.game.reset_game()
            return

        self.game.get_previous_state().match_over_update()

        self.reset_command_flags()

    def draw(self, window):
        self.match_over_banner.draw(window)
        self.command_bar.draw(window)

    def layout_ui(self):
        self.match_over_banner.rect.center = CENTER
        self.command_bar.rect.midbottom = COMMAND_BAR_MIDBOTTOM
