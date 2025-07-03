import pygame

from src.game_states.game_state import GameState
from src.input_definitions import MenuInput
from src.game_states.title_menu.title_menu import TitleMenu
from src.sounds import MENU_SELECT
from src.game_states.title.title_ui import TitleUI


class Title(GameState):

    def __init__(self, game):
        super().__init__(game)
        self.ui = TitleUI()
        
        self.commands = {
            MenuInput.SELECT: False
        }

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
               self.commands[MenuInput.SELECT] = True
                
    def update(self):
        if self.commands[MenuInput.SELECT]:
            MENU_SELECT.play()

            self.game.transition_to(TitleMenu(self.game))

        self.reset_command_flags()

    def draw(self, window):
        self.ui.draw(window)