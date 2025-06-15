import pygame

import src.config as cfg
from src.game_states.game_state import GameState
from src.input import MenuInput
from src.game_states.level_select import LevelSelect
from src.game_states.run_co_op import RunCoOp
from src.game_states.run_deathmatch import RunDeathMatch
from src.game_states.run_timed_score import RunTimedScore
from src.game_states.start import Start
from src.menu import Menu, MenuItem
import src.ui_elements as ui


class MultiplayerMenu(GameState):

    def __init__(self, game):
        super().__init__(game)

        self.multiplayer_menu_items = [
            MenuItem("Death Match", lambda: self.game.save_play_state(RunDeathMatch)),
            MenuItem("Timed Score", lambda: self.game.save_play_state(RunTimedScore)),
            MenuItem("Co-Op", lambda: self.game.save_play_state(RunCoOp))
        ]

        self.multiplayer_menu = Menu(
            items=self.multiplayer_menu_items, 
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
            self.multiplayer_menu.select()
            self.game.game_state.pop()
            # self.game.game_state.push(self.game.saved_play_state(self.game))
            self.game.game_state.push(LevelSelect(self.game))

        if self.inputs[MenuInput.LEFT] == True:
            self.multiplayer_menu.down()

        if self.inputs[MenuInput.RIGHT] == True:
            self.multiplayer_menu.up()

        self.reset_inputs()

    def draw(self, window):
        window.blit(ui.PING_PANG_SURF, ui.PING_PANG_RECT)
        window.blit(ui.TITLE_SURF, ui.TITLE_RECT) 
        self.multiplayer_menu.draw(window)
        window.blit(ui.PRESS_SPACE_SURF, ui.PRESS_SPACE_RECT)