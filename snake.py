import time

import pygame

import config as cfg
import ui_elements as ui


class Snake:

    def __init__(
        self, window_size, size=1, position=(0, 0), 
        direction=(1, 0), color=ui.rand_rgb()
    ):
        self.body = []
        self.size = size
        self.color = color
        self.display_size = (self.size - 4, self.size - 4)
        self.window_w, self.window_h = window_size
        self.initial_position = position
        self.head_position = self.initial_position
        self.initial_direction = direction
        self.direction = self.initial_direction
        self.alive = True
        self.next_move = None
        self.has_eaten = False
        self.initial_timer = .15
        self.timer = self.initial_timer
        self.timer_reducer = 1.015
        self.prev_time = time.perf_counter()
        self.score = 0
        self.fill_body()

    def fill_body(self, length=5):
        for count in range(length):
            self.body.append(
                (
                    self.head_position[0] - ((self.size * self.direction[0]) * count), 
                    self.head_position[1] - ((self.size * self.direction[1]) * count)
                )
            )

    def reset(self):
        self.moving = False
        self.head_position = self.initial_position
        self.direction = self.initial_direction
        self.timer = self.initial_timer
        self.body = []
        self.fill_body()
    

    def update(self, time_now):
        snake_dt = time_now - self.prev_time
        if snake_dt >= self.timer:
            
            self.update_direction()
            new_x = self.head_position[0] + ((self.direction[0] * self.size))
            new_y = self.head_position[1] + ((self.direction[1] * self.size))

            if self.body_collision(new_x, new_y):
                self.reset()
                # self.score = 0
                return False
            
            new_x, new_y = self.check_wrap(new_x, new_y)
            self.set_head_position((new_x, new_y))
            self.body.insert(0, self.head_position)

            if self.has_eaten:
                # self.score += len(self.body) * 10
                self.timer /= self.timer_reducer
                self.has_eaten = False
            else:
                self.body.pop(-1)
            
            self.set_prev_time(time_now)

    def draw(self, window):
        for segment in self.body:
            pygame.draw.rect(
                window, self.color, ((segment), (self.display_size))
            )

    def set_prev_time(self, time_now):
        self.prev_time = time_now
    
    def set_head_position(self, position):
        self.head_position = position

    def eat(self):
        self.has_eaten = True

    def body_collision(self, x, y):
        if (x, y) in self.body[3:]:
            return True
        return False
  
    def update_direction(self):
        if self.next_move == "up":
            if not abs(self.direction[1]):
                self.direction = (0, -1)
        elif self.next_move == "down":
            if not abs(self.direction[1]):
                self.direction = (0, 1)
        elif self.next_move == "left":
            if not abs(self.direction[0]):
                self.direction = (-1, 0)
        elif self.next_move == "right":
            if not abs(self.direction[0]):
                self.direction = (1, 0)

    def check_wrap(self, x, y):
        if self.head_position[0] >= self.window_w:
            return (0, y)
        elif self.head_position[0] < 0: 
            return (self.window_w - self.size, y)
        elif self.head_position[1] >= self.window_h:
            return (x, 0)
        elif self.head_position[1] < 0:
            return (x, self.window_h - self.size)
        return (x, y)
    