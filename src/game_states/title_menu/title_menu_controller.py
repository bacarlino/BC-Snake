from src.enums import MenuTypes
from src.game_states.run_one_player import RunOnePlayer
from src.game_states.run_co_op import RunCoOp
from src.game_states.run_deathmatch import RunDeathMatch
from src.game_states.start import Start
from src.game_states.title_menu.title_menus import build_title_menus
from src.level_config.level_config_controller import LevelConfigController
from src.stack_manager import StackManager



class TitleMenuController:

    def __init__(self, game_state, game):
        self.game = game
        self.game_state = game_state
        
        self.level_config = LevelConfigController()

        self.stack = StackManager()
        self.menus = build_title_menus(self)
        self.stack.push(self.menus[MenuTypes.PLAYERS])

    def current(self):
        return self.stack.peek()
    
    def handle_event(self, event):
        self.current().handle_event(event)
    
    def update(self):
        self.current().update()

    def draw(self, window):
        if self.current():
            self.current().draw(window)

    def close_top_menu(self):
        self.stack.pop()

    def push_menu(self, menu):
        self.stack.push(menu)
    
    def stack_has_one_item(self):
        return self.stack.has_one_item()
    
    def displays_title(self):
        return self.current().displays_title()
    
    def select_one_player(self):
        self.game.save_play_state(RunOnePlayer)
        self.stack.push(self.menus[MenuTypes.LEVEL])

    def select_two_player(self):
        self.stack.push(self.menus[MenuTypes.MULTIPLAYER])

    def select_level(self, level):
        self.game.load_level(level)
        self.game.start_game()

    def select_multiplayer_mode(self, mode):
        self.game.save_play_state(mode)
        self.stack.push(self.menus[MenuTypes.LEVEL])

    def level_menu(self):
        self.title_hidden = False

    def custom_level_menu(self):
        self.stack.push(self.menus[MenuTypes.CUSTOM])
        self.title_hidden = True

    def perimeter_on(self):
        self.stack.pop()
        self.level_config.has_border = True
        self.current().update_sub_text(self.level_config.has_border_sub_text())

    def perimeter_off(self):
        self.stack.pop()
        self.level_config.has_border = False
        self.current().update_sub_text(self.level_config.has_border_sub_text())

    def set_cell_size(self, size):
        self.stack.pop()
        self.level_config.cell_size = size
        self.top_menu.update_sub_text(self.level_config.cell_size_sub_text)

    def cell_size_small(self):
        self.stack.pop()
        self.level_config.cell_size = 16
        self.current().update_sub_text(self.level_config.cell_size_sub_text())

    def cell_size_medium(self):
        self.stack.pop()
        self.level_config.cell_size = 32
        self.current().update_sub_text(self.level_config.cell_size_sub_text())

    def cell_size_large(self):
        self.stack.pop()
        self.level_config.cell_size = 64
        self.current().update_sub_text(self.level_config.cell_size_sub_text())

    def start_speed_slow(self):
        self.stack.pop()
        self.level_config.start_speed = 6
        self.current().update_sub_text(self.level_config.start_speed_sub_text())

    def start_speed_medium(self):
        self.stack.pop()
        self.level_config.start_speed = 8
        self.current().update_sub_text(self.level_config.start_speed_sub_text())
    
    def start_speed_fast(self):
        self.stack.pop()
        self.level_config.start_speed = 10
        self.current().update_sub_text(self.level_config.start_speed_sub_text())

    def acceleration_off(self):
        self.stack.pop()
        self.level_config.acceleration = 0
        self.current().update_sub_text(self.level_config.acceleration_sub_text())

    def acceleration_low(self):
        self.stack.pop()
        self.acceleration = 1.5
        self.current().update_sub_text(self.level_config.acceleration_sub_text())

    def acceleration_high(self):
        self.stack.pop()
        self.level_config.acceleration = 2.5
        self.current().update_sub_text(self.level_config.acceleration_sub_text())
        
    def fruit_qty_low(self):
        self.stack.pop()
        self.level_config.fruit_qty = 1
        self.current().update_sub_text(self.level_config.fruit_qty_sub_text())

    def fruit_qty_medium(self):
        self.stack.pop()
        self.level_config.fruit_qty = 5
        self.current().update_sub_text(self.level_config.fruit_qty_sub_text())

    def fruit_qty_high(self):
        self.stack.pop()
        self.level_config.fruit_qty = 25
        self.current().update_sub_text(self.level_config.fruit_qty_sub_text())
    
    def growth_rate_low(self):
        self.stack.pop()
        self.level_config.growth_rate = 1
        self.current().update_sub_text(self.level_config.growth_rate_sub_text())

    def growth_rate_medium(self):
        self.stack.pop()
        self.level_config.growth_rate = 3
        self.current().update_sub_text(self.level_config.growth_rate_sub_text())

    def growth_rate_high(self):
        self.stack.pop()
        self.level_config.growth_rate = 10
        self.current().update_sub_text(self.level_config.growth_rate_sub_text())

    def start_custom_game(self):
        self.game.start_custom_game()