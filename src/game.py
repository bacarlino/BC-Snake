import random
import time

import pygame

import src.config as cfg
from src.game_states.title import Title
from src.game_states.game_over import GameOver


class Game:

    def __init__(self, window_size):
        self.window_w, self.window_h = self.window_size = window_size
        self.running = True
        self.game_state = Title(self)
        self.run_state = None

        self.cell_size = 32 # probably better in the game_state?
        self.display_size = (self.cell_size - 4, self.cell_size - 4)
    
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

    def change_state(self, state):
        self.game_state = state

    def set_run_state(self, state):
        self.run_state = state

    # Probably better in game state
    def change_cell_size(self, size):
        if self.window_w % size == 0:
            self.cell_size = size
    
    # moves to game_state - run_two_player specifically
    def check_snake_collision(self):
        snake = self.snakes[0]
        snake2 = self.snakes[1]

        if snake.head_position == snake2.head_position:
            snake.die()
            snake2.die()
            self.game_state = GameOver(self)

        if snake.head_position in snake2.body:
            snake.die()
            self.game_state = GameOver(self)

        if snake2.head_position in snake.body:
            snake2.die()
            self.game_state = GameOver(self)

    def reset_game(self):
        self.game_state = Title(self)
        self.run_state = None
        self.snakes = []
        self.scores = []
        self.fruits = []
        self.add_fruit(4)

    def reset_snakes(self):
        for index in range(len(self.snakes)):
            self.snakes[index].reset()
            self.scores[index] = 0

    def clear_snakes(self):
        self.snakes = []
        self.scores = []