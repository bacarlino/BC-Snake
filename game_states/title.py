import pygame

from .game_state import GameState
from input import Menu 
from .title_players import TitlePlayers
import ui_elements as ui

class Title(GameState):

    def __init__(self, game):
        super().__init__(game)
        self.inputs = {
            Menu.SELECT: False
        }

    def handle_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
               self.inputs[Menu.SELECT] = True
                
    def update(self):
        if self.inputs[Menu.SELECT]:
            self.game.change_state(TitlePlayers(self.game))

        self.reset_inputs()

    def draw(self, window):
        window.blit(ui.PING_PANG_SURF, ui.PING_PANG_RECT)
        window.blit(ui.TITLE_SURF, ui.TITLE_RECT)
        window.blit(ui.PRESS_SPACE_SURF, ui.PRESS_SPACE_RECT)
