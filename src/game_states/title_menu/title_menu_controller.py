from src.enums import MenuType
from src.game_states.run_one_player import RunOnePlayer
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
        self.menu_stack.push(self.menus[MenuType.PLAYERS])

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
        self.menu_stack.push(self.menus[MenuType.LEVEL])

    def select_two_player(self):
        self.menu_stack.push(self.menus[MenuType.MULTIPLAYER])

    def select_level(self, level):
        self.game.load_level(level)
        self.game.start_game()

    def select_multiplayer_mode(self, mode):
        self.game.save_play_state(mode)
        self.menu_stack.push(self.menus[MenuType.LEVEL])

    def level_menu(self):
        self.title_hidden = False

    def custom_level_menu(self):
        self.menu_stack.push(self.menus[MenuType.CUSTOM])
        self.title_hidden = True

    def set_lvl_attr(self, lvl_attr_cfg):
        print("NEW set_lvl_attr METHOD CALLED")
        self.menu_stack.pop()
        setattr(self, lvl_attr_cfg.attr, lvl_attr_cfg)
        self.current().update_sub_text(lvl_attr_cfg.name)

    def start_custom_game(self):
        self.game.start_custom_game(self.level_config.get_level_config())