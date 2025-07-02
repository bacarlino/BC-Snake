import pygame

from src.input_definitions import MenuInput
from src.game_states.game_state import GameState

from src.game_states.title_menu.title_menu_controller import TitleMenuController
import src.ui.ui_elements as ui


class TitleMenu(GameState):

    def __init__(self, game):
        super().__init__(game)

        self.commands = {MenuInput.BACK: False}

        self.menu_controller = TitleMenuController(self, self.game)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            self.menu_controller.handle_event(event)
            if event.key == pygame.K_ESCAPE:
                self.commands[MenuInput.BACK] = True
                
    def update(self):
        if self.commands[MenuInput.BACK]:
            if self.menu_controller.stack_has_one_item():
                
                #GAME
                self.game.reset_game()
                return
            else:
                self.menu_controller.close_top_menu()

        self.menu_controller.update()

        self.reset_command_flags()

    def draw(self, window):
        window.blit(ui.PING_PANG_SURF, ui.PING_PANG_RECT)
        if self.menu_controller.displays_title():
            window.blit(ui.TITLE_SURF, ui.TITLE_RECT) 
        self.menu_controller.draw(window)

        window.blit(ui.PRESS_SPACE_SURF, ui.PRESS_SPACE_RECT)
