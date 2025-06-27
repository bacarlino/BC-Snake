import pygame

from src.input import MenuInput
from src.game_states.game_state import GameState

from src.title_menu_controller import TitleMenuController
import src.ui_elements as ui


class TitleMenu(GameState):

    def __init__(self, game):
        super().__init__(game)

        self.title_hidden = False

        self.commands = {
            MenuInput.BACK: False
        }

        self.menu_controller = TitleMenuController(self, self.game)

    def handle_events(self, event):
        if event.type == pygame.KEYDOWN:
            self.menu_controller.current().handle_event(event)
            if event.key == pygame.K_ESCAPE:
                self.commands[MenuInput.BACK] = True
                
    def update(self):
        if self.commands[MenuInput.BACK]:
            if self.menu_controller.menu_stack_has_items():
                self.menu_controller.close_top_menu()
                if not self.menu_controller.menu_stack_has_items():
                    self.game.reset_game()
                    return
            else:
                self.game.reset_game()
                return

        self.menu_controller.update()

        self.reset_command_flags()

    def draw(self, window):
        window.blit(ui.PING_PANG_SURF, ui.PING_PANG_RECT)
        if self.menu_controller.displays_title():
            window.blit(ui.TITLE_SURF, ui.TITLE_RECT) 
        self.menu_controller.draw(window)

        window.blit(ui.PRESS_SPACE_SURF, ui.PRESS_SPACE_RECT)
