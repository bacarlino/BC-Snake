from src.game_states.title import Title
from src.level_config.level_config import CLASSIC
from src.stack_manager import StackManager


class GameController:
    
    def __init__(self, window_size):
        self.saved_play_state = None
        self.level_config = CLASSIC
        self.game_state_stack = StackManager()
        self.window_size = window_size
        self.display_size = None

    def reset_game(self):
        self.game_state_stack.push(Title(self))

    def update(self):
        self.game_state_stack.update()

    def save_play_state(self, play_state):
        self.saved_play_state = play_state

    def load_level(self, level):
        self.level_config = level
        self.update_display_size()