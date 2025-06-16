import pygame

import src.config as cfg
from src.input import MenuInput
from src.game_states.game_state import GameState
from src.game_states.run_one_player import RunOnePlayer
from src.game_states.run_two_player import RunTwoPlayer
from src.game_states.level_select import LevelSelect
from src.game_states.multiplayer_menu import MultiplayerMenu
from src.menu import Menu, MenuItem
from src.stack_manager import StackManager
import src.ui_elements as ui


class TitlePlayers(GameState):

    def __init__(self, game):
        super().__init__(game)
        self.menu_stack = StackManager()
        players_menu_items = [
            MenuItem("1 Player", self.select_one_player),
            MenuItem("2 Player", self.select_two_player)
        ]

        self.players_menu = Menu(
            items=players_menu_items,
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
            self.players_menu.select()

        if self.inputs[MenuInput.LEFT] == True:
            self.players_menu.down()

        if self.inputs[MenuInput.RIGHT] == True:
            self.players_menu.up()

        self.reset_inputs()

    def draw(self, window):
        window.blit(ui.PING_PANG_SURF, ui.PING_PANG_RECT)
        window.blit(ui.TITLE_SURF, ui.TITLE_RECT) 
        self.players_menu.draw(window)
        window.blit(ui.PRESS_SPACE_SURF, ui.PRESS_SPACE_RECT)

    def select_one_player(self):
        self.game.save_play_state(RunOnePlayer)
        self.game.game_state.pop()
        self.game.game_state.push(LevelSelect(self.game))

    def select_two_player(self):
        # self.game.save_play_state(RunTwoPlayer)
        self.game.game_state.pop()
        self.game.game_state.push(MultiplayerMenu(self.game))