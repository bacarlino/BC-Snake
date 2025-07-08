import pygame

from src.game_states.game_state import GameState
from src.enums import Play
from src.ui.ui_elements import PressSpaceBanner

class Start(GameState):
    
    def __init__(self, game):
        super().__init__(game)
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
            self.game.pop_game_state()
        if self.commands[Play.QUIT] == True:
            self.game.reset_game()

        self.reset_command_flags()

    def draw(self, window):
        self.press_space_banner.draw(window)