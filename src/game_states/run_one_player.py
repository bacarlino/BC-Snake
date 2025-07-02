import time

import pygame

import src.app_config as cfg
from src.input_definitions import Play, ARROW, WSAD
from src.game_states.game_state import GameState
from src.snake import Snake
import src.ui.ui_elements as ui
from src.utils import align_center_to_grid, get_rand_coord


class RunOnePlayer(GameState):

    def __init__(self, game, level_config):
        super().__init__(game)
        self.level_config = level_config
        
        # SETUP BORDER
        if self.level_config.has_border:
            self.border = ui.create_border(self.level_config.cell_size)
        else:
            self.border = None

        # SETUP SNAKES
        self.snakes = [
            Snake(
                self.game.window_size, 
                [WSAD, ARROW],
                self.level_config.cell_size, 
                align_center_to_grid(self.game.window_size, self.level_config.cell_size),           
                color=cfg.PINK, initial_speed=self.level_config.start_speed,
                acceleration=self.level_config.acceleration
            )
        ]

        for snake in self.snakes:
            snake.moving = True

        # SETUP FRUIT
        self.fruits = []
        self.add_fruit(self.level_config.fruit_qty)

        # AVAILABLE COMMANDS
        self.commands = {
            Play.START: False, 
            Play.PAUSE: False,
            Play.QUIT: False
        }

    def handle_event(self, event):

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.commands[Play.PAUSE] = True
            if event.key == pygame.K_ESCAPE:
                self.commands[Play.QUIT] = True

            for snake in self.snakes:
                snake.handle_event_keydown(event)

        keys = pygame.key.get_pressed()

    def update(self):

        if self.commands[Play.PAUSE] == True:
            self.game.push_pause()
        if self.commands[Play.QUIT] == True:
            self.game.reset_game()
            return

        time_now = time.perf_counter()
        for snake in self.snakes:
            snake.update(time_now, self.border)

            self.handle_fruit_collision(snake)

            if snake.collision_detected:
                snake.die()
                self.game.push_game_over()

        self.reset_command_flags()

    def draw(self, window):
        if self.level_config.has_border:
            ui.draw_border(window, self.border, self.level_config.cell_size)
        
        score_surf, score_rect = ui.create_score_banner(
            self.snakes[0].score
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
                snake.eat(self.level_config.growth_rate)
                snake.score += (len(snake.body) * 10)
                self.fruits.remove(fruit)
                self.add_fruit()
            
    def add_fruit(self, n=1):
        for _ in range(n):
            placed = False
            while not placed:
                coord = get_rand_coord(
                    self.game.window_size, self.level_config.cell_size
                )
                if self.border and coord in self.border: continue
                if coord in self.snakes[0].body: continue
                placed = True
                self.fruits.append(coord)

    def reset_run_state(self):
        for snake in self.snakes:
            snake.reset()
        self.fruits = []
        self.add_fruit(3)