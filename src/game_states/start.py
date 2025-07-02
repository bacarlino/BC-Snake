import pygame

from src.game_states.game_state import GameState
from src.input import Play
import src.ui_elements as ui

class Start(GameState):
    
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
            self.game.game_state.pop()
        if self.commands[Play.QUIT] == True:
            self.game.reset_game()

        self.reset_command_flags()

    def draw(self, window):
        # self.game.game_state.peek_below().draw(window)
        window.blit(ui.PRESS_SPACE_SURF, ui.PRESS_SPACE_RECT)