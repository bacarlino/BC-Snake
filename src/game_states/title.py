import pygame

from src.game_states.game_state import GameState
from src.input import Menu 
from src.game_states.title_players import TitlePlayers
import src.ui_elements as ui

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
            self.game.game_state.pop()
            self.game.game_state.push(TitlePlayers(self.game))

        self.reset_inputs()

    def draw(self, window):
        window.blit(ui.PING_PANG_SURF, ui.PING_PANG_RECT)
        window.blit(ui.TITLE_SURF, ui.TITLE_RECT)
        window.blit(ui.PRESS_SPACE_SURF, ui.PRESS_SPACE_RECT)
