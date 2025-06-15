import pygame

from src.game_states.game_state import GameState
from src.input import Menu
from src.game_states.run_coop import RunCoop
from src.game_states.run_deathmatch import RunDeathmatch
from src.game_states.run_timed_score import RunTimedScore
from src.game_states.start import Start
import src.ui_elements as ui


class MultiplayerMenu(GameState):

    def __init__(self, game):
        super().__init__(game)
        self.level_selection = None
        self.menu = ui.multiplayer_menu

        self.multiplayer_choices = (
            RunDeathmatch,
            RunTimedScore,
            RunCoop
        )

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
            self.game.load_level(self.level_choices[self.menu.index])
            self.game.game_state.pop()
            self.game.game_state.push(self.game.run_state(self.game))
            self.game.game_state.push(Start(self.game))

        if self.inputs[Menu.LEFT] == True:
            self.menu.down()

        if self.inputs[Menu.RIGHT] == True:
            self.menu.up()

        self.reset_inputs()

    def draw(self, window):
        window.blit(ui.PING_PANG_SURF, ui.PING_PANG_RECT)
        window.blit(ui.TITLE_SURF, ui.TITLE_RECT) 
        self.menu.draw(window)
        window.blit(ui.PRESS_SPACE_SURF, ui.PRESS_SPACE_RECT)