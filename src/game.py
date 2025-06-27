import pygame

import src.app_config as cfg
from src.game_states.title import Title
import src.level_config.level_config as levels
from src.stack_manager import StackManager


class Game:

    def __init__(self, window_size):
        self.window_w, self.window_h = self.window_size = window_size
        self.running = True
        self.saved_play_state = None

        self.level_config = levels.CLASSIC
        self.display_size = None
        self.update_display_size()
        
        self.game_state = StackManager()
        self.game_state.push(Title(self))
    

    def run(self, window):
        clock = pygame.time.Clock()
        while self.running:
            window.fill(cfg.BLACK)
            self.handle_events()
            self.update()
            self.draw(window)
            pygame.display.flip()
            clock.tick(120)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            self.game_state.handle_events(event)

    def update(self):
        self.game_state.update()
          
    def draw(self, window):
        self.game_state.draw(window)

    def load_level(self, level):
        self.level_config = level
        self.update_display_size()

    def save_play_state(self, play_state):
        self.saved_play_state = play_state

    def update_display_size(self):
        self.display_size = (self.level_config.cell_size - 4, self.level_config.cell_size - 4)

    def change_cell_size(self, size):
        if self.window_w % size == 0:
            self.level_config.cell_size = size

    def reset_game(self):
        self.game_state.push(Title(self))

    def load_level_config(self, level_config):
        self.level_config = level_config

    def pop_game_state(self):
        self.game_state.pop()