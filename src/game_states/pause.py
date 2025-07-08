import pygame

from src.game_states.game_state import GameState
from src.enums import Play
from src.ui.ui_elements import PausedBanner, PressSpaceBanner

class Pause(GameState):
    
    def __init__(self, game):
        super().__init__(game)
        self.paused_banner = PausedBanner()
        self.command_bar = PressSpaceBanner()
        self.commands = {
            Play.PAUSE: False,
            Play.QUIT: False
        }

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.commands[Play.PAUSE] = True
            if event.key == pygame.K_ESCAPE:
                self.commands[Play.QUIT] = True
                
    def update(self):
        if self.commands[Play.PAUSE] == True:
            self.game.pop_game_state()
        if self.commands[Play.QUIT] == True:
            self.game.reset_game()
            return

        self.reset_command_flags()

    def draw(self, window):
        self.paused_banner.draw(window)
        self.command_bar.draw(window)