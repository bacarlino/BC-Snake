from abc import ABC, abstractmethod
from enum import Enum, auto


class State(Enum):
    TITLE = auto()
    TITLE_PLAYERS = auto()
    START = auto()
    PLAYING = auto()
    PAUSED = auto()
    LOSS = auto()


class GameState(ABC):
    
    def __init__(self, game):
        self.game = game
        self.inputs = {}

    @abstractmethod
    def handle_events(self, event):
        pass

    @abstractmethod
    def update(self):
        self.reset_inputs()

    @abstractmethod
    def draw(self, window):
        pass

    def reset_inputs(self):
        for command in self.inputs:
            self.inputs[command] = False
