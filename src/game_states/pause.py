import pygame

from src.game_states.game_state import GameState
from src.controls import Play
import src.ui_elements as ui

class Pause(GameState):
    
    def __init__(self, game):
        super().__init__(game)
        self.inputs = {
            Play.PAUSE: False,
            Play.QUIT: False
        }

    def handle_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.inputs[Play.PAUSE] = True
            if event.key == pygame.K_ESCAPE:
                self.inputs[Play.QUIT] = True
                
    def update(self):
        if self.inputs[Play.PAUSE] == True:
            self.game.game_state.pop()
        if self.inputs[Play.QUIT] == True:
            self.game.reset_game()
            return

        self.reset_inputs()

    def draw(self, window):
        self.game.game_state.peek_below().draw(window)
        window.blit(ui.PRESS_SPACE_SURF, ui.PRESS_SPACE_RECT)