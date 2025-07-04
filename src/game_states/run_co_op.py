import time

import pygame

import src.config as cfg
from src.input import Play, ARROW, WSAD
from src.game_states.game_over import GameOver
from src.game_states.game_state import GameState
from src.game_states.pause import Pause
from src.snake import Snake
import src.ui_elements as ui
from src.utils import get_rand_coord


class RunCoOp(GameState):

    def __init__(self, game):
        super().__init__(game)

        # BORDER
        if self.game.level_config.has_border:
            self.border = ui.create_border(self.game.level_config.cell_size)
        else:
            self.border = []

        # SNAKES
        self.snakes = [
            Snake(
                self.game.window_size, 
                [ARROW],
                self.game.level_config.cell_size, 
                ((self.game.window_w * .75), self.game.window_h // 2),           
                (0, 1), color=cfg.PINK, initial_speed=self.game.level_config.speed,
                acceleration = self.game.level_config.acceleration
            ),
            Snake(
                self.game.window_size, 
                [WSAD],
                self.game.level_config.cell_size, 
                ((self.game.window_w * .25), (self.game.window_h // 2) - self.game.level_config.cell_size),
                (0, -1), color=cfg.PURPLE, initial_speed=self.game.level_config.speed,
                acceleration = self.game.level_config.acceleration
            )
        ]

        for snake in self.snakes:
            snake.moving = True
        
        # FRUIT
        self.fruits = []
        self.add_fruit(self.game.level_config.fruit_qty)

        # AVAILABLE INPUTS
        self.commands = {
            Play.START: False, 
            Play.PAUSE: False,
            Play.QUIT: False
        }

    def handle_events(self, event):

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.commands[Play.PAUSE] = True
            if event.key == pygame.K_ESCAPE:
                self.commands[Play.QUIT] = True

        keys = pygame.key.get_pressed()

        for snake in self.snakes:
            snake.handle_keys(keys)

    def update(self):

        if self.inputs[Play.PAUSE] == True:
            self.game.game_state.push(Pause(self.game))
        if self.inputs[Play.QUIT] == True:
            self.game.reset_game()
            return
        
        time_now = time.perf_counter()
        
        for snake in self.snakes:
            other_snakes = self.snakes.copy()
            other_snakes.remove(snake)

            snake.update(time_now, self.border, other_snakes)

            if snake.collision_detected:
                snake.die()
            
            self.handle_fruit_collision(snake)

        if all([snake.dead for snake in self.snakes]):
            # snake.moving = False
            self.game.game_state.push(GameOver(self.game))

        self.reset_command_flags()

    def draw(self, window):
        ui.draw_border(window, self.border, self.game.level_config.cell_size)
        
        score_surf, score_rect = ui.create_score_banner(
            self.snakes[0].score + self.snakes[1].score
        )
        window.blit(score_surf, score_rect)

        for fruit in self.fruits:
            pygame.draw.rect(
                window, cfg.GREEN, ((fruit), (self.game.display_size)), border_radius=cfg.BORDER_RADIUS
            )
        for snake in self.snakes:
            snake.draw(window)

    def handle_fruit_collision(self, snake):
        for fruit in self.fruits:
            if fruit == snake.head_position:
                snake.eat(self.game.level_config.growth_rate)
                snake.score += (len(snake.body) * 10)
                self.fruits.remove(fruit)
                self.add_fruit()
            
    def add_fruit(self, n=1):
        for _ in range(n):
            placed = False
            while not placed:
                coord = get_rand_coord(self.game.window_size, self.game.level_config.cell_size)
                if self.border and coord in self.border: continue
                if coord in self.snakes[0].body: continue
                if coord in self.snakes[1].body: continue
                placed = True
                self.fruits.append(coord)

    def reset_run_state(self):
        for snake in self.snakes:
            snake.reset()
        self.fruits = []
        self.add_fruit(3)