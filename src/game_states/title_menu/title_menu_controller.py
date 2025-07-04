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

    def set_border(self, attribute):
        self.stack.pop()
        self.level_config.has_border = attribute
        self.current().update_sub_text(attribute.name)

    def set_cell_size(self, attribute):
        self.stack.pop()
        self.level_config.cell_size = attribute
        self.current().update_sub_text(attribute.name)

    def set_start_speed(self, attribute):
        self.stack.pop()
        self.level_config.start_speed = attribute
        self.current().update_sub_text(attribute.name)

    def set_acceleration(self, attribute):
        self.stack.pop()
        self.level_config.acceleration = attribute
        self.current().update_sub_text(attribute.name)

    def set_fruit_qty(self, attribute):
        self.stack.pop()
        self.level_config.fruit_qty = attribute
        self.current().update_sub_text(attribute.name)
    
    def set_growth_rate(self, attribute):
        self.stack.pop()
        self.level_config.growth_rate = attribute
        self.current().update_sub_text(attribute.name)

    def start_custom_game(self):
        self.game.start_custom_game(self.level_config.get_level_config())