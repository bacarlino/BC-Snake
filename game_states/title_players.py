import pygame

from .game_state import GameState
from ..input import Menu
from .run_one_player import RunOnePlayer
from .run_two_player import RunTwoPlayer
from .start import Start

from .. import ui_elements as ui

class TitlePlayers(GameState):

    def __init__(self, game):
        super().__init__(self, game)
        self.inputs = {
            Menu.SELECT: False,
            Menu.LEFT: False,
            Menu.RIGHT: False
        }

    def handle_events(self, event):
        for key in self.inputs:
            self.inputs[key] = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.inputs[Menu.SELECT] = True
            if event.key == pygame.K_LEFT:
                self.inputs[Menu.LEFT]= True
            if event.key == pygame.K_RIGHT:
                self.inputs[Menu.RIGHT] = True
                
    def update(self):
        if self.inputs[Menu.SELECT] == True:
            self.game.change_state(Start(self.game))
            self._space_pressed = False

        if self.inputs[Menu.LEFT] == True:
            self.game.set_players(1)
            self.game.set_run_state(RunOnePlayer(self.game))
            ui.players_menu.down()
            self._left_pressed = False

        if self.inputs[Menu.RIGHT] == True:
            self.game.set_players(2)
            self.game.set_run_state(RunTwoPlayer(self.game))
            self._right_pressed = False

        self.reset_inputs()

    def draw(self, window):
        window.blit(ui.PING_PANG_SURF, ui.PING_PANG_RECT)
        window.blit(ui.TITLE_SURF, ui.TITLE_RECT) 
        ui.players_menu.draw(window)
        window.blit(ui.PRESS_SPACE_SURF, ui.PRESS_SPACE_RECT)