import time

import pygame

from src.config import BORDER_RADIUS
from src.sounds import EAT_FRUIT_SFX, COLLISION_SFX
import src.ui_elements as ui


class Snake:

    def __init__(
        self, window_size, cell_size=1, position=(0, 0), 
        direction=(1, 0), initial_speed=5, acceleration=0, color=ui.rand_rgb(),
        length=5
    ):
        self.cell_size = cell_size
        self.display_size = (self.cell_size - 4, self.cell_size - 4)
        self.main_color = color
        self.current_color = color
        self.flash_colors = [self.main_color, (230, 230, 230)]
        
        self.body = []
        self.length = self.initial_length = length
        self.has_eaten = False
        self.belly = 0
        self.score = 0

        self.window_w, self.window_h = window_size
        self.initial_position = position
        self.head_position = self.initial_position

        self.moving = False
        self.initial_direction = direction
        self.direction = self.initial_direction
        self.next_direction = None

        self.initial_speed = initial_speed
        self.speed = initial_speed
        self.move_timer = 1 / self.speed
        self.acceleration = acceleration
        self.prev_move_time = time.perf_counter()

        self.collision_detected = False
        self.dead = False
        self.prev_flash_time = self.prev_move_time
        
        self.fill_body(self.length)


    def fill_body(self, length=5):
        for count in range(length):
            self.body.append(
                (
                    self.head_position[0] - ((self.cell_size * self.direction[0]) * count), 
                    self.head_position[1] - ((self.cell_size * self.direction[1]) * count)
                )
            )

    def reset(self):
        self.moving = True
        self.collision_detected = False
        self.dead = False
        self.current_color = self.main_color
        self.head_position = self.initial_position
        self.direction = self.initial_direction
        self.speed = self.initial_speed
        self.move_timer = 1 / self.speed
        self.body = []
        # self.score = 0
        self.fill_body()
    

    def update(self, time_now, border=None, other_snakes=None):
        if self.dead:
            self.moving = False
            self.update_dead(time_now)
            return

        move_dt = time_now - self.prev_move_time
        if move_dt >= self.move_timer and self.moving:
            
            # updates self.direction using self.next_direction
            self.update_direction()

            # calculate move
            new_x = self.head_position[0] + ((self.direction[0] * self.cell_size))
            new_y = self.head_position[1] + ((self.direction[1] * self.cell_size))

            # check for collisions
            if (new_x, new_y) in self.body[3:]:
                self.collision_detected = True
                return
            
            if border and (new_x, new_y) in border:
                self.collision_detected = True
                return
            
            if other_snakes:
                for snake in other_snakes:
                    if (new_x, new_y) in snake.body:
                        self.collision_detected = True
                        if (new_x, new_y) == snake.head_position:
                            snake.collision_detected = True
                        return
    
            # handle screen wrap
            new_x, new_y = self.check_wrap(new_x, new_y)

            # if all is good finally set the new head position
            self.set_head_position((new_x, new_y))
            self.body.insert(0, self.head_position)

            # if there's not a fruit, pop the tail
            if self.belly:
                self.belly -= 1
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
        main_body = pygame.Rect((self.head_position), (self.display_size))
        head_mark = main_body.copy()
        deflate = self.display_size[0] * -0.5
        head_mark.inflate_ip(deflate, deflate)
        pygame.draw.rect(
            window, self.current_color, main_body, border_radius=BORDER_RADIUS
        )
        pygame.draw.rect(
            window, (230, 230, 230), head_mark, border_radius=BORDER_RADIUS
        )
        for segment in self.body[1:]:
            pygame.draw.rect(
                window, self.current_color, (segment, self.display_size), border_radius=BORDER_RADIUS
            )

    def set_prev_move_time(self, time_now):
        self.prev_move_time = time_now
    
    def set_head_position(self, position):
        self.head_position = position

    def eat(self, qty):
        EAT_FRUIT_SFX.play()
        self.belly += qty
        self.increase_speed()
    
    def increase_speed(self):
        self.speed *= 1 + self.acceleration / 100
        self.move_timer = 1 / self.speed

    def die(self):
        COLLISION_SFX.play()
        self.dead = True

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
            return (self.window_w - self.cell_size, y)
        elif self.head_position[1] >= self.window_h:
            return (x, 0)
        elif self.head_position[1] < 0:
            return (x, self.window_h - self.cell_size)
        return (x, y)

    def add_score(self, score):
        self.score += score