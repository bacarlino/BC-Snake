import time

import pygame

from src.sounds import EAT_FRUIT_SFX, COLLISION_SFX
import src.ui_elements as ui


class Snake:

    def __init__(
        self, window_size, size=1, position=(0, 0), 
        direction=(1, 0), color=ui.rand_rgb()
    ):
        self.body = []
        self.size = size
        self.main_color = color
        self.current_color = color
        self.display_size = (self.size - 4, self.size - 4)
        self.window_w, self.window_h = window_size
        self.initial_position = position
        self.head_position = self.initial_position
        self.initial_direction = direction
        self.direction = self.initial_direction
        self.next_direction = None
        self.collide = False
        self.has_eaten = False
        self.initial_move_timer = .15
        self.move_timer = self.initial_move_timer
        self.move_timer_reducer = 1.015
        self.prev_move_time = time.perf_counter()
        self.score = 0
        self.dead = False
        self.flash_timer = .1
        self.prev_flash_time = self.prev_move_time
        self.fill_body()

        self.flash_colors = [self.main_color, (230, 230, 230)]

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
        self.collide = False
        self.dead = False
        self.current_color = self.main_color
        self.head_position = self.initial_position
        self.direction = self.initial_direction
        self.move_timer = self.initial_move_timer
        self.body = []
        self.fill_body()
    

    def update(self, time_now, border=None, other_snake=None):
  

        move_dt = time_now - self.prev_move_time
        if move_dt >= self.move_timer:
            
            # updates self.direction using self.next_direction
            self.update_direction()

            # calculate move
            new_x = self.head_position[0] + ((self.direction[0] * self.size))
            new_y = self.head_position[1] + ((self.direction[1] * self.size))

            # check for collisions
            if self.body_collision(new_x, new_y):
                self.collide = True
                return
            
            if border:
                if self.border_collision(new_x, new_y, border):
                    self.collide = True
                    return
                
            # if other_snake:
            #     if self.snake_collision(new_x, new_y, other_snake):
            #         self.collide = True
            #         return
            #     if self.headon_collision(new_x, new_y, other_snake):
            #         self.collide = True
            #         other_snake.collide = True
            #         return
                
            
            # hand screen wrap
            new_x, new_y = self.check_wrap(new_x, new_y)

            # if all is good finally set the new head position
            self.set_head_position((new_x, new_y))
            self.body.insert(0, self.head_position)

            # if there's not a fruit, pop the tail
            if self.has_eaten:
                self.move_timer /= self.move_timer_reducer
                self.has_eaten = False
            else:
                self.body.pop(-1)
            # reset the move timer
            self.set_prev_move_time(time_now)

    def update_dead(self, time_now):
        flash_dt = time_now - self.prev_flash_time
        if flash_dt >= 0.1:
            self.current_color = self.flash_colors.pop()
            self.flash_colors.insert(0, self.current_color)
            self.prev_flash_time = time_now

    def draw(self, window):

        for segment in self.body:
            pygame.draw.rect(
                window, self.current_color, ((segment), (self.display_size))
            )

    def set_prev_move_time(self, time_now):
        self.prev_move_time = time_now
    
    def set_head_position(self, position):
        self.head_position = position

    def eat(self):
        EAT_FRUIT_SFX.play()
        self.has_eaten = True

    def die(self):
        COLLISION_SFX.play()
        self.dead = True

    def body_collision(self, x, y):
        if (x, y) in self.body[3:]:
            return True
        return False
    
    def border_collision(self, x, y, border_list):
        if (x, y) in border_list:
            return True
        return False

    def snake_collision(self, x, y, other_snake):
        if (x, y) in other_snake.body:
            return True
        return False

    def headon_collision(self, x, y, other_snake):
        if (x, y) == other_snake.head_position:
            return True
        return False
    
    def update_direction(self):
        if self.next_direction == "up":
            if not abs(self.direction[1]):
                self.direction = (0, -1)
        elif self.next_direction == "down":
            if not abs(self.direction[1]):
                self.direction = (0, 1)
        elif self.next_direction == "left":
            if not abs(self.direction[0]):
                self.direction = (-1, 0)
        elif self.next_direction == "right":
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
