import pygame

import src.config as cfg
from src.controls import MenuInput
from src.game_states.game_state import GameState
from src.game_states.run_one_player import RunOnePlayer
from src.game_states.run_co_op import RunCoOp
from src.game_states.run_deathmatch import RunDeathMatch
from src.game_states.run_score_battle import RunScoreBattle
import src.level_config as levels
from src.menu import Menu, MenuItem
from src.stack_manager import StackManager
from src.game_states.start import Start
import src.ui_elements as ui


class TitleMenu(GameState):

    def __init__(self, game):
        super().__init__(game)

        players_menu_items = [
            MenuItem("1 Player", self.select_one_player),
            MenuItem("2 Player", self.select_two_player)
        ]

        self.level_menu_items = [
            MenuItem("Classic", lambda: self.select_level(levels.CLASSIC)),
            MenuItem("Big", lambda: self.select_level(levels.BIG)),
            MenuItem("Super", lambda: self.select_level(levels.SUPER)),
            MenuItem("Extreme", lambda: self.select_level(levels.EXTREME)), 
            MenuItem("Insane", lambda: self.select_level(levels.INSANE))
        ]

        self.multiplayer_menu_items = [
            MenuItem(
                "Death\nMatch", 
                lambda: self.select_multiplayer_mode(RunDeathMatch)
            ),
            MenuItem(
                "Score\nBattle", 
                lambda: self.select_multiplayer_mode(RunScoreBattle)
            ),
            MenuItem(
                "Co-Op", 
                lambda: self.select_multiplayer_mode(RunCoOp)
            )

        ]

        menu_args = {
            "index": 0, 
            "pos": (cfg.CENTER[0], cfg.WINDOW_H * 0.75), 
            "size": (1000, 150), 
            "main_font": ui.MENU_FONT, 
            "highlight_font": ui.HIGHTLIGHT_FONT,
            "background": cfg.BLACK, 
            "main_color": cfg.PINK, 
            "highlight_color": cfg.WHITE
        }

        self.players_menu = Menu(players_menu_items, **menu_args)
        self.level_menu = Menu(self.level_menu_items, **menu_args)
        self.multiplayer_menu = Menu(
            self.multiplayer_menu_items, **menu_args
        )

        self.menu = StackManager()
        self.menu.push(self.players_menu)

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
            self.menu.peek().select()

        if self.inputs[MenuInput.LEFT] == True:
            self.menu.peek().down()

        if self.inputs[MenuInput.RIGHT] == True:
            self.menu.peek().up()

        self.reset_inputs()

    def draw(self, window):
        window.blit(ui.PING_PANG_SURF, ui.PING_PANG_RECT)
        window.blit(ui.TITLE_SURF, ui.TITLE_RECT) 
        if self.menu.peek():
            self.menu.peek().draw(window)
        window.blit(ui.PRESS_SPACE_SURF, ui.PRESS_SPACE_RECT)

    def select_one_player(self):
        self.game.save_play_state(RunOnePlayer)
        self.menu.push(self.level_menu)

    def select_two_player(self):
        self.menu.push(self.multiplayer_menu)

    def select_level(self, level):
        self.game.load_level(level)
        self.game.game_state.pop()
        self.game.game_state.push(self.game.saved_play_state(self.game))
        self.game.game_state.push(Start(self.game))

    def select_multiplayer_mode(self, mode):
        self.game.save_play_state(mode)
        self.menu.push(self.level_menu)