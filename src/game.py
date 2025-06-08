import random
import time

import pygame

import config as cfg
from game_states.title import Title
from game_states.game_over import GameOver


class Game:

    def __init__(self, window_size):
        self.window_w, self.window_h = self.window_size = window_size
        self.running = True
        self.game_state = Title(self)
        self.run_state = None
        self.cell_size = 32
        self.display_size = (self.cell_size - 4, self.cell_size - 4)
        self.snakes = []
        self.scores = []
        self.fruits = []
        self.add_fruit(4)
    
    def run(self, window):
        clock = pygame.time.Clock()
        while self.running:
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
        window.fill(cfg.BACKGROUND_COLOR)
        self.game_state.draw(window)

    def change_state(self, state):
        self.game_state = state

    def set_run_state(self, state):
        self.run_state = state

    def change_cell_size(self, size):
        if self.window_w % size == 0:
            self.cell_size = size

    def add_snake(self, snake):  
        self.snakes.append(snake)
        self.scores.append(0)
                         
    def update_fruit(self, snake, score_index):
        fruit_hit = self.check_hit_fruit(snake)
        if fruit_hit:
            snake.eat()
            self.scores[score_index] += len(snake.body) * 10
            self.remove_fruit(fruit_hit)
            self.add_fruit()
    
    def check_snake_collision(self):
        snake = self.snakes[0]
        snake2 = self.snakes[1]

        if snake.head_position == snake2.head_position:
            self.game_state = GameOver(self)

        if snake.head_position in snake2.body:
            self.game_state = GameOver(self)

        if snake2.head_position in snake.body:
            self.game_state = GameOver(self)

    def add_fruit(self, n=1):
        for _ in range(n):
            rand_x = random.randint(0, (self.window_size[0] // self.cell_size) - 1)                          
            rand_y = random.randint(0, (self.window_size[1] // self.cell_size) - 1)
            
            conflict = False

            for snake in self.snakes:
                if (rand_x, rand_y) in snake.body:
                    conflict = True
            if not conflict:
                self.fruits.append(
                    (rand_x * self.cell_size, rand_y * self.cell_size)
                )
            else:
                self.add_fruit()
        
    def check_hit_fruit(self, snake):
        for fruit in self.fruits:
            if fruit == snake.head_position:
                return fruit
                            
    def remove_fruit(self, fruit):
        self.fruits.remove(fruit)

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