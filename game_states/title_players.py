import pygame

from .game_state import GameState
from input import Menu
from .run_one_player import RunOnePlayer
from .run_two_player import RunTwoPlayer
from .start import Start
import ui_elements as ui


class TitlePlayers(GameState):

    def __init__(self, game):
        super().__init__(game)
        self.run_state_selection = RunOnePlayer(self.game)
        self.inputs = {
            Menu.SELECT: False,
            Menu.LEFT: False,
            Menu.RIGHT: False
        }

    def handle_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.inputs[Menu.SELECT] = True
            if event.key == pygame.K_LEFT:
                self.inputs[Menu.LEFT] = True
            if event.key == pygame.K_RIGHT:
                self.inputs[Menu.RIGHT] = True
                
    def update(self):
        
        if self.inputs[Menu.SELECT] == True:
            self.game.set_run_state(self.run_state_selection)
            self.game.change_state(Start(self.game))

        if self.inputs[Menu.LEFT] == True:
            self.run_state_selection = RunOnePlayer(self.game)
            ui.players_menu.down()

        if self.inputs[Menu.RIGHT] == True:
            self.run_state_selection = RunTwoPlayer(self.game)
            ui.players_menu.up()

        self.reset_inputs()

    def draw(self, window):
        window.blit(ui.PING_PANG_SURF, ui.PING_PANG_RECT)
        window.blit(ui.TITLE_SURF, ui.TITLE_RECT) 
        ui.players_menu.draw(window)
        window.blit(ui.PRESS_SPACE_SURF, ui.PRESS_SPACE_RECT)