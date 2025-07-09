import pygame

from src.enums import MenuInput
from src.game_states.game_state import GameState

from src.game_states.title_menu.title_menu_controller import TitleMenuController
from src.game_states.title_menu.title_menu_ui import TitleMenuUI
from src.ui.ui_elements import NameBanner, TitleBanner, PressSpaceEscBanner


class TitleMenu(GameState):

    def __init__(self, game):
        super().__init__(game)

        self.commands = {MenuInput.BACK: False}
        self.menu_controller = TitleMenuController(self, self.game)

        self.ui = TitleMenuUI(self.menu_controller.current())

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            self.menu_controller.handle_event(event)
            if event.key == pygame.K_ESCAPE:
                self.commands[MenuInput.BACK] = True
                
    def update(self):
        if self.commands[MenuInput.BACK]:
            if self.menu_controller.stack_has_one_item():
                self.game.reset_game()
                return
            else:
                self.menu_controller.close_top_menu()
                
        self.menu_controller.update()
        self.reset_command_flags()

    def draw(self, window):
        self.ui.draw(window)

    def update_ui(self):
        self.ui.update_menu(self.menu_controller.current())