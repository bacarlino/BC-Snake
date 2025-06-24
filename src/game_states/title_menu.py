import pygame

import src.app_config as cfg
from src.input import MenuInput
from src.game_states.game_state import GameState
from src.game_states.run_one_player import RunOnePlayer
from src.game_states.run_co_op import RunCoOp
from src.game_states.run_deathmatch import RunDeathMatch
from src.game_states.run_score_battle import RunScoreBattle
from src.level_config.level_config import create_level_config
from src.menus.menu import Menu, MenuGrid, MenuItem
from src.menus.title_menus import build_title_menus
from src.stack_manager import StackManager
from src.game_states.start import Start
import src.ui_elements as ui


class TitleMenu(GameState):

    def __init__(self, game):
        super().__init__(game)

        self.title_hidden = False

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

        self.menus = build_title_menus(self)
        self.menu = StackManager()
        self.menu.push(self.menus["players"])

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
        if self.menu.peek().show_title():
            window.blit(ui.TITLE_SURF, ui.TITLE_RECT) 
        if self.menu.peek():
            self.menu.peek().draw(window)
        window.blit(ui.PRESS_SPACE_SURF, ui.PRESS_SPACE_RECT)

    def select_one_player(self):
        self.game.save_play_state(RunOnePlayer)
        self.menu.push(self.menus["level"])

    def select_two_player(self):
        self.menu.push(self.menus["multiplayer"])

    def select_level(self, level):
        self.game.load_level(level)
        self.game.game_state.pop()
        self.game.game_state.push(self.game.saved_play_state(self.game))
        self.game.game_state.push(Start(self.game))

    def select_multiplayer_mode(self, mode):
        self.game.save_play_state(mode)
        self.menu.push(self.menus["level"])

    def level_menu(self):
        self.title_hidden = False

    def custom_level_menu(self):
        self.menu.push(self.menus["custom"])
        self.title_hidden = True

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
        level_params = create_level_config(
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
            return "Big"
        
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
