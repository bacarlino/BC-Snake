import pygame

from src.game_states.game_state import GameState
from src.input import MenuInput
from src.game_states.title_menu import TitleMenu
from src.sounds import MENU_SELECT
from src.ui_elements import TitleUI


class Title(GameState):

    def __init__(self, game):
        super().__init__(game)
        self.ui = TitleUI()

        
        self.commands = {
            MenuInput.SELECT: False
        }

    def handle_events(self, event):
        # invoker??
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
               self.commands[MenuInput.SELECT] = True
                
    def update(self):
        if self.commands[MenuInput.SELECT]:
            MENU_SELECT.play()
            self.game.game_state.pop()
            self.game.game_state.push(TitleMenu(self.game))

        self.reset_command_flags()

    def draw(self, window):
        self.ui.draw(window)
        # window.blit(ui.PING_PANG_SURF, ui.PING_PANG_RECT)
        # window.blit(ui.TITLE_SURF, ui.TITLE_RECT)
        # window.blit(ui.PRESS_SPACE_SURF, ui.PRESS_SPACE_RECT)

        

class PushTitleMenu:
    def __init__(self, state):
        self.state = state

    def execute(self):
        MENU_SELECT.play()
        self.state.game.game_state.pop()
        self.game.game_state.push(TitleMenu(self.game))

