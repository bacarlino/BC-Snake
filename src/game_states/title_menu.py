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

        # CUSTOM LEVEL OPTIONS
        self.has_border = True
        self.start_speed = 6
        self.acceleration = 0
        self.cell_size = 32
        self.fruit_qty = 1
        self.growth_rate = 1 


        # MENUS
        menu_height = ui.PRESS_SPACE_RECT.top - ui.TITLE_RECT.bottom 
        self.menu = StackManager()
        menu_pos = (ui.TITLE_RECT.midbottom)
        menu_size = (cfg.WINDOW_W * 0.9, menu_height)
        menu_colors = {            
            "main_font": ui.MENU_FONT, 
            "highlight_font": ui.HIGHTLIGHT_FONT,
            "sub_font": ui.SUB_FONT,
            "main_color": cfg.PINK, 
            "highlight_color": cfg.WHITE,
            "sub_color": cfg.AQUA,
            "bg_color": cfg.BLACK, 
        }

        # PLAYER MENU
        players_menu_items = [
            MenuItem("1 Player", self.select_one_player, sub_text=None),
            MenuItem("2 Player", self.select_two_player, sub_text=None)
        ]
        self.players_menu = Menu(players_menu_items, menu_pos, menu_size, **menu_colors)

        # LEVEL SELECT MENU
        level_menu_items = [
            MenuItem(
                "Classic",
                lambda: self.select_level(levels.CLASSIC),
                "The classic snake experience",
            ),     
            MenuItem(
                "Zooomed",
                lambda: self.select_level(levels.BIG),
                "Zooomed in. Classic with a twist - ZOOM"
            ),
            MenuItem(
                "Super\nClassic",
                lambda: self.select_level(levels.SUPER),
                "More Fruit. More Growth. More Speed.",
            ),
            MenuItem(
                "Extreme",
                lambda: self.select_level(levels.EXTREME), 
                "Everything turned up to 11 on a large map",
            ),
        
            MenuItem(
                "Insane",
                lambda: self.select_level(levels.INSANE),
                "What even is this?"
            ),
           
            MenuItem(
                "Custom",
                lambda: self.menu.push(self.custom_level_menu),
                "Create your own game",
            )
        ]
        self.level_menu = Menu(level_menu_items, menu_pos, menu_size, **menu_colors)

        # MULTIPLAYER MENU
        multiplayer_menu_items = [
            MenuItem(
                "Death\nMatch", 
                lambda: self.select_multiplayer_mode(RunDeathMatch),
                "Score when the other snake dies. 3 to win"
            ),
            MenuItem(
                "Score\nBattle", 
                lambda: self.select_multiplayer_mode(RunScoreBattle),
                "Highest score held when the first snake dies wins"
            ),
            MenuItem(
                "Co-Op", 
                lambda: self.select_multiplayer_mode(RunCoOp),
                "Work together to get a high score"
            )
        ]
        self.multiplayer_menu = Menu(
            multiplayer_menu_items, menu_pos, menu_size, **menu_colors
        )

        # CUSTOM LEVEL MENU
        custom_level_items = [
            MenuItem(
                "Perimeter\nWall", 
                lambda: self.menu.push(self.perimeter_menu),
                f"{self.has_border_sub_text()}"
            ),
            MenuItem(
                "World\nSize",
                lambda: self.menu.push(self.cell_size_menu),
                f"{self.cell_size_sub_text()}"
            ),
            MenuItem(
                "Start\nSpeed",
                lambda: self.menu.push(self.start_speed_menu),
                f"{self.start_speed_sub_text()}"
            ),
            MenuItem(
                "Speed\nUp", 
                lambda: self.menu.push(self.acceleration_menu),
                f"{self.acceleration_sub_text()}"
            ),
            MenuItem(
                "Fruit\nQuantity", 
                lambda: self.menu.push(self.fruit_qty_menu),
                f"{self.fruit_qty_sub_text()}"
            ),
            MenuItem(
                "Growth\nRate",
                lambda: self.menu.push(self.growth_rate_menu),
                f"{self.growth_rate_sub_text()}"
            ),
            MenuItem(
                "Start\nGame",
                self.start_custom_game,
                "Confirm Settings"
            ),
            
        ]
        self.custom_level_menu = Menu(custom_level_items, menu_pos, menu_size, **menu_colors)
       
        perimeter_menu_items = [
            MenuItem("On", self.perimeter_on, sub_text=None),
            MenuItem("Off", self.perimeter_off, sub_text=None)
        ]
        self.perimeter_menu = Menu(perimeter_menu_items, menu_pos, menu_size, **menu_colors)

        cell_size_menu_items = [
            MenuItem("Big", self.cell_size_large, sub_text=None),
            MenuItem("Medium", self.cell_size_medium, sub_text=None),
            MenuItem("Small", self.cell_size_small, sub_text=None),
        ]
        self.cell_size_menu = Menu(cell_size_menu_items, menu_pos, menu_size, **menu_colors)

        start_speed_menu_items = [
            MenuItem("Slow", self.start_speed_slow, sub_text=None),
            MenuItem("Medium", self.start_speed_medium, sub_text=None),
            MenuItem("Fast", self.start_speed_fast, sub_text=None)
        ]
        self.start_speed_menu = Menu(start_speed_menu_items, menu_pos, menu_size, **menu_colors)

        acceleration_menu_items = [
            MenuItem("Off", self.acceleration_off, sub_text=None),
            MenuItem("Low", self.acceleration_low, sub_text=None),
            MenuItem("High", self.acceleration_high, sub_text=None)
        ]
        
        self.acceleration_menu = Menu(acceleration_menu_items, menu_pos, menu_size, **menu_colors)

        fruit_qty_menu_items = [
            MenuItem("Low", self.fruit_qty_low, sub_text=None),
            MenuItem("Medium", self.fruit_qty_medium, sub_text=None),
            MenuItem("High", self.fruit_qty_high, sub_text=None)
        ]
        self.fruit_qty_menu = Menu(fruit_qty_menu_items, menu_pos, menu_size, **menu_colors)

        growth_rate_menu_items = [
            MenuItem("Low", self.growth_rate_low, sub_text=None),
            MenuItem("Medium", self.growth_rate_medium, sub_text=None),
            MenuItem("High", self.growth_rate_high, sub_text=None)
        ]
        self.growth_rate_menu = Menu(growth_rate_menu_items, menu_pos, menu_size, **menu_colors)

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
        self.menu.peek().update_sub_text(self.has_border_sub_text())

    def perimeter_off(self):
        self.menu.pop()
        self.has_border = False
        self.menu.peek().update_sub_text(self.has_border_sub_text())

    def cell_size_small(self):
        self.menu.pop()
        self.cell_size = 16
        self.menu.peek().update_sub_text(self.cell_size_sub_text())

    def cell_size_medium(self):
        self.menu.pop()
        self.cell_size = 32
        self.menu.peek().update_sub_text(self.cell_size_sub_text())

    def cell_size_large(self):
        self.menu.pop()
        self.cell_size = 64
        self.menu.peek().update_sub_text(self.cell_size_sub_text())

    def start_speed_slow(self):
        self.menu.pop()
        self.start_speed = 6
        self.menu.peek().update_sub_text(self.start_speed_sub_text())

    def start_speed_medium(self):
        self.menu.pop()
        self.start_speed = 8
        self.menu.peek().update_sub_text(self.start_speed_sub_text())
    
    def start_speed_fast(self):
        self.menu.pop()
        self.start_speed = 10
        self.menu.peek().update_sub_text(self.start_speed_sub_text())

    def acceleration_off(self):
        self.menu.pop()
        self.acceleration = 0
        self.menu.peek().update_sub_text(self.acceleration_sub_text())

    def acceleration_low(self):
        self.menu.pop()
        self.acceleration = 1.5
        self.menu.peek().update_sub_text(self.acceleration_sub_text())

    def acceleration_high(self):
        self.menu.pop()
        self.acceleration = 2.5
        self.menu.peek().update_sub_text(self.acceleration_sub_text())
        
    def fruit_qty_low(self):
        self.menu.pop()
        self.fruit_qty = 1
        self.menu.peek().update_sub_text(self.fruit_qty_sub_text())

    def fruit_qty_medium(self):
        self.menu.pop()
        self.fruit_qty = 5
        self.menu.peek().update_sub_text(self.fruit_qty_sub_text())

    def fruit_qty_high(self):
        self.menu.pop()
        self.fruit_qty = 25
        self.menu.peek().update_sub_text(self.fruit_qty_sub_text())
    
    def growth_rate_low(self):
        self.menu.pop()
        self.growth_rate = 1
        self.menu.peek().update_sub_text(self.growth_rate_sub_text())

    def growth_rate_medium(self):
        self.menu.pop()
        self.growth_rate = 3
        self.menu.peek().update_sub_text(self.growth_rate_sub_text())

    def growth_rate_high(self):
        self.menu.pop()
        self.growth_rate = 10
        self.menu.peek().update_sub_text(self.growth_rate_sub_text())

    def start_custom_game(self):
        level_params = levels.create_level_config(
            self.has_border,
            self.start_speed,
            self.acceleration,
            self.cell_size,
            self.fruit_qty,
            self.growth_rate
        )
        self.game.load_level(level_params)
        self.game.game_state.pop()
        self.game.game_state.push(self.game.saved_play_state(self.game))
        self.game.game_state.push(Start(self.game))

    def has_border_sub_text(self):
        return "On" if self.has_border else "Off"
    
    def cell_size_sub_text(self):
        print(f"Cell Size: {self.cell_size}")
        if self.cell_size == 16:
            return "Small"
        elif self.cell_size == 32:
            return "Medium"
        elif self.cell_size == 64:
            return "Large"
        
    def start_speed_sub_text(self):
        print(f"Start Speed: {self.start_speed}")
        if self.start_speed == 6:
            return "Slow"
        elif self.start_speed == 8:
            return "Medium"
        elif self.start_speed == 10:
            return "Fast"

    def acceleration_sub_text(self):
        print("Speed up: ", self.acceleration)
        if self.acceleration == 0:
            return "Off"
        elif self.acceleration == 1.5:
            return "Low"
        elif self.acceleration == 2.5:
            return "High"
        else:
            return "Error"
     
    def fruit_qty_sub_text(self):
        print("Fruit qty: ", self.fruit_qty)
        if self.fruit_qty == 1:
            return "Low"
        elif self.fruit_qty == 5:
            return "Medium"
        elif self.fruit_qty == 25:
            return "High"
        
    def growth_rate_sub_text(self):
        if self.growth_rate == 1:
            return "Low"
        elif self.growth_rate == 3:
            return "Medium"
        elif self.growth_rate == 10:
            return "High"
