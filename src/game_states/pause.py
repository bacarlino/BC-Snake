import pygame

from src.game_states.game_state import GameState
from src.input import Play
import src.ui_elements as ui

class Pause(GameState):
    
    def __init__(self, game):
        super().__init__(game)
        self.commands = {
            Play.PAUSE: False,
            Play.QUIT: False
        }

    def handle_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.comands[Play.PAUSE] = True
            if event.key == pygame.K_ESCAPE:
                self.comands[Play.QUIT] = True
                
    def update(self):
        if self.comands[Play.PAUSE] == True:
            self.game.game_state.pop()
        if self.comands[Play.QUIT] == True:
            self.game.reset_game()
            return

        self.reset_comand_flags()

    def draw(self, window):
        self.game.game_state.peek_below().draw(window)
        window.blit(ui.PRESS_SPACE_SURF, ui.PRESS_SPACE_RECT)