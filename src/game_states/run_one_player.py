import random
import time

import pygame

import src.config as cfg
from src.input import Play
from src.game_states.game_over import GameOver
from src.game_states.game_state import GameState
from src.game_states.pause import Pause
from src.snake import Snake
import src.ui_elements as ui


class RunOnePlayer(GameState):

    def __init__(self, game):
        super().__init__(game)
        self.border = ui.create_border(self.game.cell_size)
        self.snake = Snake(
                self.game.window_size, self.game.cell_size, 
                (self.game.window_w // 2, self.game.window_h // 2),           
                color=cfg.PINK
            )
        self.fruits = []
        self.cell_size = 32
        self.add_fruit(4)

        self.inputs = {
            Play.SNAKE_ONE_UP: False,
            Play.SNAKE_ONE_DOWN: False,
            Play.SNAKE_ONE_LEFT: False,
            Play.SNAKE_ONE_RIGHT: False,
            Play.START: False, 
            Play.PAUSE: False,
            Play.QUIT: False
        }

    def handle_events(self, event):

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.inputs[Play.PAUSE] = True
            if event.key == pygame.K_ESCAPE:
                self.inputs[Play.QUIT] = True


        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_UP]:
            self.inputs[Play.SNAKE_ONE_UP] = True
        elif keys[pygame.K_DOWN]:
            self.inputs[Play.SNAKE_ONE_DOWN] = True
        elif keys[pygame.K_LEFT]:
            self.inputs[Play.SNAKE_ONE_LEFT] = True
        elif keys[pygame.K_RIGHT]:
            self.inputs[Play.SNAKE_ONE_RIGHT] = True


    def update(self):

        if self.inputs[Play.PAUSE] == True:
            self.game.change_state(Pause(self.game))
        if self.inputs[Play.QUIT] == True:
            self.game.reset_game()
            return


        if self.inputs[Play.SNAKE_ONE_UP]:
            self.snake.next_direction = "up"
        if self.inputs[Play.SNAKE_ONE_DOWN]:
            self.snake.next_direction = "down"
        if self.inputs[Play.SNAKE_ONE_LEFT]:
            self.snake.next_direction = "left"
        if self.inputs[Play.SNAKE_ONE_RIGHT]:
            self.snake.next_direction = "right"


        time_now = time.perf_counter()
        self.snake.update(time_now, self.border)
        self.update_fruit()

        if self.snake.collide:
            self.snake.die()
            self.game.change_state(GameOver(self.game))

        self.reset_inputs()

    def draw(self, window):
        SCORE_BANNER_SURF, SCORE_BANNER_RECT = ui.create_score_banner(
            self.snake.score
        )
        window.blit(SCORE_BANNER_SURF, SCORE_BANNER_RECT)

        for fruit in self.fruits:
            pygame.draw.rect(
                window, cfg.LIME, ((fruit), (self.game.display_size))
            )

        ui.draw_border(window, self.border, self.cell_size)
        
        self.snake.draw(window)
        
    def update_fruit(self):
        fruit_hit = self.check_hit_fruit()
        if fruit_hit:
            self.snake.eat()
            self.snake.add_score(len(self.snake.body) * 10)
            self.remove_fruit(fruit_hit)
            self.add_fruit()

    def check_hit_fruit(self):
        for fruit in self.fruits:
            if fruit == self.snake.head_position:
                return fruit
            
    def add_fruit(self, n=1):
        for _ in range(n):
            rand_x = random.randint(0, (self.game.window_size[0] // self.cell_size) - 1)                          
            rand_y = random.randint(0, (self.game.window_size[1] // self.cell_size) - 1)
            
            conflict = False

            if (rand_x, rand_y) in self.snake.body:
                conflict = True

            if not conflict:
                self.fruits.append(
                    (rand_x * self.cell_size, rand_y * self.cell_size)
                )
            else:
                self.add_fruit()

    def remove_fruit(self, fruit):
        self.fruits.remove(fruit)
