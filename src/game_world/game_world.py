import time

import pygame

from src.ui.ui_config import BORDER_RADIUS, GREEN
from src.utils import get_rand_coord

class GameWorld:

    def __init__(
        self, window_size, display_size, snakes, border, level_config, scores
    ):
        self.window_size = window_size
        self.display_size = display_size
        self.snakes = snakes
        self.border = border
        self.level_config = level_config
        self.fruits = []
        self.scores = scores
        self.fruit_score_strategy = None

        self.set_snakes_moving()
        self.add_fruit(level_config.fruit_qty)

    def set_fruit_score_strategy(self, strategy_fn):
        self.score_strategy = strategy_fn

    def handle_event(self, event):
        for snake in self.snakes:
            snake.handle_event_keydown(event)

    def update(self):
        if self.update_snakes(): return True

    def update_snakes(self):
        time_now = time.perf_counter()

        for snake in self.snakes:
            other_snakes = self.other_snakes(snake)
            snake.update(time_now, self.border, other_snakes)
            self.handle_snake_collision(snake)
            self.handle_fruit_collision(snake)

    def update_snakes_no_collision(self):
        time_now = time.perf_counter()
        for snake in self.snakes:
            snake.update(time_now)
        
    def reset_snakes(self):
        for snake in self.snakes:
            snake.reset()

    def draw(self, window):
        if self.border:
            self.border.draw(window)
        self.draw_fruit(window)
        self.draw_snakes(window)

    def draw_snakes(self, window):
        for snake in self.snakes:
            snake.draw(window)

    def draw_fruit(self, window):
        for fruit in self.fruits:
            pygame.draw.rect(
                window, GREEN, ((fruit), (self.display_size)), border_radius=BORDER_RADIUS
            )

    def set_snakes_moving(self):
        for snake in self.snakes:
            snake.moving = True

    def handle_snake_collision(self, snake):
        for snake in self.snakes:
            if not snake.dead:
                if snake.collision_detected:
                    snake.die()

    def other_snakes(self, snake):
        return [
            other for other in self.snakes if other is not snake
        ]

    def all_snake_segments_list(self):
        return [segment for snake in self.snakes for segment in snake.body]
    
    def any_snake_dead(self):
        return any([snake.dead for snake in self.snakes])

    def all_snakes_dead(self):
        return all([snake.dead for snake in self.snakes])
    
    def add_fruit(self, n=1):
        for _ in range(n):
            placed = False
            while not placed:
                coord = get_rand_coord(
                    self.window_size, self.level_config.cell_size
                )
                if self.border and coord in self.border.coord_list: continue
               
                if coord in self.all_snake_segments_list(): 
                    continue

                placed = True
                self.fruits.append(coord)
    
    def handle_fruit_collision(self, snake):
        if snake.head_position in self.fruits:
            snake.eat(self.level_config.growth_rate)
            self.score_strategy(snake, self.scores)
            self.fruits.remove(snake.head_position)
            self.add_fruit()