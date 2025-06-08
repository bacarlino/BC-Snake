import pygame

from .game_state import GameState
from input import Play
import ui_elements as ui

class Start(GameState):
    
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
            self.game.change_state(self.game.run_state)
        if self.inputs[Play.QUIT] == True:
            self.game.reset_game()

        self.reset_inputs()

    def draw(self, window):
        self.game.run_state.draw(window)
        window.blit(ui.PRESS_SPACE_SURF, ui.PRESS_SPACE_RECT)