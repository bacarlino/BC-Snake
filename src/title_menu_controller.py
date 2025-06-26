from src.game_states.run_one_player import RunOnePlayer
from src.game_states.run_co_op import RunCoOp
from src.game_states.run_deathmatch import RunDeathMatch
from src.game_states.start import Start
from src.menus.title_menus import build_title_menus
import src.level_config.level_config as levels
from src.level_config.level_config import create_level_config
from src.level_config.level_config_controller import LevelConfigController
from src.stack_manager import StackManager



class TitleMenuController:

    def __init__(self, game_state, game):
        self.game = game
        self.game_state = game_state
        
        self.level_config = LevelConfigController()

        self.stack = StackManager()
        self.menus = build_title_menus(self)
        self.stack.push(self.menus["players"])


    def current(self):
        return self.stack.peek()
    
    def update(self):
        self.current().update()

    def draw(self, window):
        if self.current():
            self.current().draw(window)

    def nav_up(self):
        if self.stack.has_items() > 1:
            self.stack.pop()

    def displays_title(self):
        return self.current().displays_title()
    
    def select_one_player(self):
        self.game.save_play_state(RunOnePlayer)
        self.stack.push(self.menus["level"])

    def select_two_player(self):
        self.stack.push(self.menus["multiplayer"])

    def select_level(self, level):
        self.game.load_level(level)
        self.game.game_state.pop()
        self.game.game_state.push(self.game.saved_play_state(self.game))
        self.game.game_state.push(Start(self.game))

    def select_multiplayer_mode(self, mode):
        self.game.save_play_state(mode)
        self.stack.push(self.menus["level"])

    def level_menu(self):
        self.title_hidden = False

    def custom_level_menu(self):
        self.stack.push(self.menus["custom"])
        self.title_hidden = True

    def perimeter_on(self):
        self.menu.pop()
        self.level_config.has_border = True
        self.stack.peek().update_sub_text(self.level_config.has_border_sub_text())

    def perimeter_off(self):
        self.stack.pop()
        self.level_config.has_border = False
        self.stack.peek().update_sub_text(self.level_config.has_border_sub_text())

    def cell_size_small(self):
        self.stack.pop()
        self.cell_size = 16
        self.stack.peek().update_sub_text(self.cell_size_sub_text())

    def cell_size_medium(self):
        self.stack.pop()
        self.cell_size = 32
        self.stack.peek().update_sub_text(self.cell_size_sub_text())

    def cell_size_large(self):
        self.stack.pop()
        self.cell_size = 64
        self.stack.peek().update_sub_text(self.cell_size_sub_text())

    def start_speed_slow(self):
        self.stack.pop()
        self.start_speed = 6
        self.stack.peek().update_sub_text(self.start_speed_sub_text())

    def start_speed_medium(self):
        self.stack.pop()
        self.start_speed = 8
        self.stack.peek().update_sub_text(self.start_speed_sub_text())
    
    def start_speed_fast(self):
        self.stack.pop()
        self.start_speed = 10
        self.stack.peek().update_sub_text(self.start_speed_sub_text())

    def acceleration_off(self):
        self.stack.pop()
        self.acceleration = 0
        self.stack.peek().update_sub_text(self.acceleration_sub_text())

    def acceleration_low(self):
        self.stack.pop()
        self.acceleration = 1.5
        self.stack.peek().update_sub_text(self.acceleration_sub_text())

    def acceleration_high(self):
        self.stack.pop()
        self.acceleration = 2.5
        self.stack.peek().update_sub_text(self.acceleration_sub_text())
        
    def fruit_qty_low(self):
        self.stack.pop()
        self.fruit_qty = 1
        self.stack.peek().update_sub_text(self.fruit_qty_sub_text())

    def fruit_qty_medium(self):
        self.stack.pop()
        self.fruit_qty = 5
        self.stack.peek().update_sub_text(self.fruit_qty_sub_text())

    def fruit_qty_high(self):
        self.stack.pop()
        self.fruit_qty = 25
        self.stack.peek().update_sub_text(self.fruit_qty_sub_text())
    
    def growth_rate_low(self):
        self.stack.pop()
        self.growth_rate = 1
        self.stack.peek().update_sub_text(self.growth_rate_sub_text())

    def growth_rate_medium(self):
        self.stack.pop()
        self.growth_rate = 3
        self.stack.peek().update_sub_text(self.growth_rate_sub_text())

    def growth_rate_high(self):
        self.stack.pop()
        self.growth_rate = 10
        self.stack.peek().update_sub_text(self.growth_rate_sub_text())

    def start_custom_game(self):
        level_params = create_level_config(
            self.level_config.has_border,
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