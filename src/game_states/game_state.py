from abc import ABC, abstractmethod


class GameState(ABC):
    
    def __init__(self, game):
        self.game = game
        self.commands = {}

    @abstractmethod
    def handle_events(self, event):
        pass

    @abstractmethod
    def update(self):
        self.reset_inputs()

    @abstractmethod
    def draw(self, window):
        pass

    def reset_command_flags(self):
        for command in self.commands:
            self.commands[command] = False
