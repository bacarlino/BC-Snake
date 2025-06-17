import pygame

import src.config as cfg
from src.controls import MenuInput
from src.game_states.game_state import GameState
from src.game_states.start import Start
import src.level_config as levels
from src.menu import Menu, MenuItem

import src.ui_elements as ui


class LevelSelect(GameState):

    def __init__(self, game):
        super().__init__(game)

        self.level_menu_items = [
            MenuItem("Classic", lambda: self.game.load_level(levels.CLASSIC)),
            MenuItem("Big", lambda: self.game.load_level(levels.BIG)),
            MenuItem("Super", lambda: self.game.load_level(levels.SUPER)),
            MenuItem("Extreme", lambda: self.game.load_level(levels.EXTREME)), 
            MenuItem("Insane", lambda: self.game.load_level(levels.INSANE))
        ]

        self.level_menu = Menu(
            items=self.level_menu_items, 
            index=0, 
            pos=(cfg.CENTER[0], cfg.WINDOW_H * 0.75), 
            size=(1000, 150), 
            main_font=ui.MENU_FONT, 
            highlight_font=ui.HIGHTLIGHT_FONT,
            background=cfg.BLACK, 
            main_color=cfg.PINK, 
            highlight_color=cfg.WHITE
        )

        self.inputs = {
            MenuInput.SELECT: False,
            MenuInput.LEFT: False,
            MenuInput.RIGHT: False
        }

    def handle_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.inputs[MenuInput.SELECT] = True
            if event.key == pygame.K_LEFT:
                self.inputs[MenuInput.LEFT] = True
            if event.key == pygame.K_RIGHT:
                self.inputs[MenuInput.RIGHT] = True
                
    def update(self):

        if self.inputs[MenuInput.SELECT] == True:
            self.level_menu.select()
            self.game.game_state.pop()
            self.game.game_state.push(self.game.saved_play_state(self.game))
            self.game.game_state.push(Start(self.game))

        if self.inputs[MenuInput.LEFT] == True:
            self.level_menu.down()

        if self.inputs[MenuInput.RIGHT] == True:
            self.level_menu.up()

        self.reset_inputs()

    def draw(self, window):
        window.blit(ui.PING_PANG_SURF, ui.PING_PANG_RECT)
        window.blit(ui.TITLE_SURF, ui.TITLE_RECT) 
        self.level_menu.draw(window)
        window.blit(ui.PRESS_SPACE_SURF, ui.PRESS_SPACE_RECT)