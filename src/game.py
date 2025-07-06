import pygame

import src.app_config as cfg
from src.game_states.game_over import GameOver
from src.game_states.pause import Pause
from src.game_states.title.title import Title
from src.game_states.start import Start
from src.stack_manager import StackManager


class Game:

    def __init__(self, window_size):
        self.window_w, self.window_h = self.window_size = window_size
        self.running = True
        self.saved_play_state = None

        self.level_config = None
        self.display_size = None
        
        self.game_state = StackManager()
        self.game_state.push(Title(self))
    

    def run(self, window):
        clock = pygame.time.Clock()
        while self.running:
            self.handle_event()
            self.update()
            self.draw(window)
            clock.tick(120)

    def handle_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            self.game_state.handle_event(event)

    def update(self):
        self.game_state.update()
          
    def draw(self, window):
        window.fill(cfg.BLACK)
        
        for game_state in self.game_state.stack:
            game_state.draw(window)

        pygame.display.flip()

    def transition_to(self, state):
        self.game_state.transition_to(state)

    def push_game_state(self, state):
        self.game_state.push(state)

    def push_game_over(self):
        self.game_state.push(GameOver(self))

    def push_pause(self):
        self.game_state.push(Pause(self))

    def load_level(self, level):
        self.level_config = level
        self.update_display_size()
    
    def start_game(self):
        self.game_state.clear()
        self.game_state.push(self.saved_play_state(self, self.level_config))
        self.game_state.push(Start(self))

    def next_round(self):
        self.pop_game_state()
        self.push_game_state(Start(self))

    def save_play_state(self, play_state):
        self.saved_play_state = play_state

    def update_display_size(self):
        self.display_size = (self.level_config.cell_size - 4, self.level_config.cell_size - 4)

    def change_cell_size(self, size):
        if self.window_w % size == 0:
            self.level_config.cell_size = size

    def reset_game(self):
        self.game_state.clear()
        self.game_state.push(Title(self))

    def pop_game_state(self):
        self.game_state.pop()

    def start_custom_game(self, level_config):
        self.load_level(level_config)
        self.start_game()