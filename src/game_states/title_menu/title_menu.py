import pygame

from src.enums import MenuInput
from src.game_states.game_state import GameState

from src.game_states.title_menu.title_menu_controller import TitleMenuController
import src.ui.ui_elements as ui
from src.ui.ui_elements import NameBanner, TitleBanner, PressSpaceEscBanner


class TitleMenu(GameState):

    def __init__(self, game):
        super().__init__(game)

        self.commands = {MenuInput.BACK: False}
        self.menu_controller = TitleMenuController(self, self.game)


        self.name_banner = NameBanner()
        self.title_banner = TitleBanner()
        self.press_space_banner = PressSpaceEscBanner()

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
        self.name_banner.draw(window)
        self.title_banner.draw(window)
        self.menu_controller.draw(window)
        self.press_space_banner.draw(window)