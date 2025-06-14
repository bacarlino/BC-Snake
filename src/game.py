import random
import time

import pygame

import src.config as cfg
from src.game_states.title import Title
from src.state_manager import StateManager


class Game:

    def __init__(self, window_size):
        self.window_w, self.window_h = self.window_size = window_size
        self.running = True
        self.run_state = None
        self.cell_size = 32
        self.display_size = (self.cell_size - 4, self.cell_size - 4)
        self.game_state = StateManager()

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

    def change_cell_size(self, size):
        if self.window_w % size == 0:
            self.cell_size = size

    def reset_game(self):
        self.game_state.push(Title(self))
