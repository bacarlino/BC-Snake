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

        self.menu_stack = StackManager()
        self.menus = build_title_menus(self)
        self.menu_stack.push(self.menus[MenuTypes.PLAYERS])

    def current(self):
        return self.menu_stack.peek()
    
    def handle_event(self, event):
        self.current().handle_event(event)
    
    def update(self):
        self.current().update()

    def draw(self, window):
        if self.current():
            self.current().draw(window)

    def close_top_menu(self):
        self.menu_stack.pop()

    def push_menu(self, menu):
        self.menu_stack.push(menu)
    
    def stack_has_one_item(self):
        return self.menu_stack.has_one_item()
    
    def displays_title(self):
        return self.current().displays_title()
    
    def select_one_player(self):
        self.game.save_play_state(RunOnePlayer)
        self.menu_stack.push(self.menus[MenuTypes.LEVEL])

    def select_two_player(self):
        self.menu_stack.push(self.menus[MenuTypes.MULTIPLAYER])

    def select_level(self, level):
        self.game.load_level(level)
        self.game.start_game()

    def select_multiplayer_mode(self, mode):
        self.game.save_play_state(mode)
        self.menu_stack.push(self.menus[MenuTypes.LEVEL])

    def level_menu(self):
        self.title_hidden = False

    def custom_level_menu(self):
        self.menu_stack.push(self.menus[MenuTypes.CUSTOM])
        self.title_hidden = True

    def set_border(self, lvl_cfg_option):
        self.menu_stack.pop()
        self.level_config.has_border = lvl_cfg_option
        self.current().update_sub_text(lvl_cfg_option.name)

    def set_cell_size(self, lvl_cfg_option):
        self.menu_stack.pop()
        self.level_config.cell_size = lvl_cfg_option
        self.current().update_sub_text(lvl_cfg_option.name)

    def set_start_speed(self, lvl_cfg_option):
        self.menu_stack.pop()
        self.level_config.start_speed = lvl_cfg_option
        self.current().update_sub_text(lvl_cfg_option.name)

    def set_acceleration(self, lvl_cfg_option):
        self.menu_stack.pop()
        self.level_config.acceleration = lvl_cfg_option
        self.current().update_sub_text(lvl_cfg_option.name)

    def set_fruit_qty(self, lvl_cfg_option):
        self.menu_stack.pop()
        self.level_config.fruit_qty = lvl_cfg_option
        self.current().update_sub_text(lvl_cfg_option.name)
    
    def set_growth_rate(self, lvl_cfg_option):
        self.menu_stack.pop()
        self.level_config.growth_rate = lvl_cfg_option
        self.current().update_sub_text(lvl_cfg_option.name)

    def start_custom_game(self):
        self.game.start_custom_game(self.level_config.get_level_config())