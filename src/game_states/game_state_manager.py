from src.level_config.level_config_controller import LevelConfigController
from src.stack_manager import StackManager


class GameStateManager(StackManager):
    
    def __init__(self, default):
        super().__init__()
        self.default_state = default
        self.play_state = None
        self.level_config_controller = LevelConfigController()
        self.level = self.level_config_controller.get_level_config()
        self.push(self.default_state)

    
    def reset_game(self):
        self.push(self.default_state)