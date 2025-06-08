import pygame

from .game_state import GameState
from ..input import Play
from .. import ui_elements as ui

class Start(GameState):
    
    def __init__(self, game):
        super().__init__(self, game)
        self.inputs = {
            Play.START: False
        }

    def handle_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.inputs[Play.START] = True
                
    def update(self):
        if self.inputs[Play.START] == True:
            self.game.change_state(self.game.run_state)

        self.reset_inputs()

    def draw(self, window):
        self.game.run_state.draw(window)
        window.blit(ui.PRESS_SPACE_SURF, ui.PRESS_SPACE_RECT)