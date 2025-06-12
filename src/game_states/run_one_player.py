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
from src.utils import get_rand_coord


class RunOnePlayer(GameState):

    def __init__(self, game):
        super().__init__(game)
        self.border = ui.create_border(self.game.cell_size)
        self.snakes = [
            Snake(
                self.game.window_size, self.game.cell_size, 
                (self.game.window_w // 2, self.game.window_h // 2),           
                color=cfg.PINK
            )
        ]
        self.fruits = []
        self.add_fruit(3)

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
            self.snakes[0].next_direction = "up"
        if self.inputs[Play.SNAKE_ONE_DOWN]:
            self.snakes[0].next_direction = "down"
        if self.inputs[Play.SNAKE_ONE_LEFT]:
            self.snakes[0].next_direction = "left"
        if self.inputs[Play.SNAKE_ONE_RIGHT]:
            self.snakes[0].next_direction = "right"


        time_now = time.perf_counter()
        self.snakes[0].update(time_now, self.border)
        self.handle_fruit_collision()

        if self.snakes[0].collide:
            self.snakes[0].die()
            self.game.change_state(GameOver(self.game))

        self.reset_inputs()

    def draw(self, window):
        ui.draw_border(window, self.border, self.game.cell_size)
        # SCORE_BANNER_SURF, SCORE_BANNER_RECT = ui.create_score_banner(
        #     self.snakes[0].score
        # )
        window.blit(*ui.create_score_banner(
            self.snakes[0].score
            )
        )
        for fruit in self.fruits:
            pygame.draw.rect(
                window, cfg.GREEN, ((fruit), (self.game.display_size))
            )
        self.snakes[0].draw(window)

    def handle_fruit_collision(self):
        for fruit in self.fruits:
            if fruit == self.snakes[0].head_position:
                self.snakes[0].eat()
                self.snakes[0].score += (len(self.snakes[0].body) * 10)
                self.fruits.remove(fruit)
                self.add_fruit()
            
    def add_fruit(self, n=1):
        for _ in range(n):
            placed = False
            while not placed:
                coord = get_rand_coord(self.game.window_size, self.game.cell_size)
                if self.border:
                    if coord in self.border: continue
                for snake in self.snakes:
                    if not coord in snake.body:
                        placed = True
                        self.fruits.append((coord[0], coord[1]))
