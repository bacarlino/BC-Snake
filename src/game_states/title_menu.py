import pygame

import src.config as cfg
from src.input import MenuInput
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

        self.commands = {
            MenuInput.BACK: False
        }

        self.menu = StackManager()
        menu_config = {
            "index": 0, 
            "pos": (cfg.CENTER[0], cfg.WINDOW_H * 0.75), 
            "size": (1000, 150), 
            "main_font": ui.MENU_FONT, 
            "highlight_font": ui.HIGHTLIGHT_FONT,
            "sub_font": ui.SUB_FONT,
            "main_color": cfg.PINK, 
            "highlight_color": cfg.WHITE,
            "background": cfg.BLACK, 
        }

        # PLAYER MENU
        players_menu_items = [
            MenuItem("1 Player", self.select_one_player),
            MenuItem("2 Player", self.select_two_player)
        ]
        self.players_menu = Menu(players_menu_items, **menu_config)

        # LEVEL SELECT MENU
        level_menu_items = [
            MenuItem(
                "Classic",
                lambda: self.select_level(levels.CLASSIC),
                "The classic snake experience",
            ),     
            MenuItem(
                "Big\nGrid",
                lambda: self.select_level(levels.BIG),
                "Small world with slight acceleration"
            ),
            MenuItem(
                "Super\nClassic",
                lambda: self.select_level(levels.SUPER),
                "More Fruit. More Growth. More Speed.",
            ),
            MenuItem(
                "Extreme",
                lambda: self.select_level(levels.EXTREME), 
                "Everything turned to 11 on a large map",
            ),
        
            # MenuItem("Insane", lambda: self.select_level(levels.INSANE)),
            MenuItem(
                "Custom",
                lambda: self.menu.push(self.custom_level_menu),
                "Create your own game",
            )
        ]
        self.level_menu = Menu(level_menu_items, **menu_config)

        # MULTIPLAYER MENU
        multiplayer_menu_items = [
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
        self.multiplayer_menu = Menu(
            multiplayer_menu_items, **menu_config
        )

        # CUSTOM LEVEL SETTINGS
        self.has_border = True,
        self.speed = 6,
        self.acceleration = 0,
        self.cell_size = 32,
        self.fruit_qty = 3,
        self.growth_rate = 1 

        # CUSTOM LEVEL MENU
        custom_level_items = [
            MenuItem(
                "Perimeter\nWall", 
                lambda: self.menu.push(self.perimeter_menu)
            ),
            MenuItem(
                "World\nSize",
                lambda: self.menu.push(self.world_size_menu)
            ),
            MenuItem(
                "Start\nSpeed",
                lambda: self.menu.push(self.start_speed_menu)
            ),
            MenuItem(
                "Speed\nUp", 
                lambda: self.menu.push(self.speed_up_menu)
            ),
            MenuItem(
                "Fruit\nQuantity", 
                lambda: self.menu.push(self.fruit_qty_menu)
            ),
            MenuItem(
                "Growth\nRate",
                lambda: self.menu.push(self.growth_rate_menu)
            ),
        ]
        self.custom_level_menu = Menu(custom_level_items, **menu_config)

        perimeter_menu_items = [
            MenuItem("On", self.perimeter_on),
            MenuItem("Off", self.perimeter_off)
        ]
        self.perimeter_menu = Menu(perimeter_menu_items, **menu_config)

        world_size_menu_items = [
            MenuItem("Small", self.world_size_small),
            MenuItem("Medium", self.world_size_medium),
            MenuItem("Large", self.world_size_large)
        ]
        self.world_size_menu = Menu(world_size_menu_items, **menu_config)

        start_speed_menu_items = [
            MenuItem("Slow", self.start_speed_slow),
            MenuItem("Medium", self.start_speed_medium),
            MenuItem("Fast", self.start_speed_fast)
        ]
        self.start_speed_menu = Menu(start_speed_menu_items, **menu_config)

        speed_up_menu_items = [
            MenuItem("On", self.speed_up_on),
            MenuItem("Off", self.speed_up_off)
        ]
        self.speed_up_menu = Menu(speed_up_menu_items, **menu_config)

        fruit_qty_menu_items = [
            MenuItem("Low", self.fruit_qty_low),
            MenuItem("Medium", self.fruit_qty_medium),
            MenuItem("High", self.fruit_qty_high)
        ]
        self.fruit_qty_menu = Menu(fruit_qty_menu_items, **menu_config)

        growth_rate_menu_items = [
            MenuItem("Low", self.growth_rate_low),
            MenuItem("Medium", self.growth_rate_medium),
            MenuItem("High", self.growth_rate_high)
        ]
        self.growth_rate_menu = Menu(growth_rate_menu_items, **menu_config)

        self.menu.push(self.players_menu)



    def handle_events(self, event):
        if event.type == pygame.KEYDOWN:
            self.menu.peek().handle_event(event)
            if event.key == pygame.K_ESCAPE:
                self.commands[MenuInput.BACK] = True
                
    def update(self):
        if self.commands[MenuInput.BACK]:
            if len(self.menu.stack) > 1:
                self.menu.pop()
        self.menu.peek().update()

        self.reset_command_flags()

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

    def perimeter_on(self):
        self.menu.pop()
        self.has_border = True

    def perimeter_off(self):
        self.menu.pop()
        self.has_border = False

    def world_size_small(self):
        self.menu.pop()
        self.world_size = 64

    def world_size_medium(self):
        self.menu.pop()
        self.world_size = 32

    def world_size_large(self):
        self.menu.pop()
        self.world_size = 64

    def start_speed_slow(self):
        self.menu.pop()
        self.start_speed = 5

    def start_speed_medium(self):
        self.menu.pop()
        self.start_speed = 8
    
    def start_speed_fast(self):
        self.menu.pop()
        self.start_speed = 12

    def speed_up_on(self):
        self.menu.pop()
        self.acceleration = True

    def speed_up_off(self):
        self.menu.pop()
        self.acceleration = False
        
    def fruit_qty_low(self):
        self.menu.pop()
        self.fruit_qty = 1

    def fruit_qty_medium(self):
        self.menu.pop()
        self.fruit_qty = 5

    def fruit_qty_high(self):
        self.menu.pop()
        self.fruit_qty = 25
    
    def growth_rate_low(self):
        self.menu.pop()
        self.growth_rate = 1

    def growth_rate_medium(self):
        self.menu.pop()
        self.growth_rate = 3

    def growth_rate_high(self):
        self.menu.pop()
        self.growth_rate = 10