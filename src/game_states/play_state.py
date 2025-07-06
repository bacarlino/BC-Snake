from abc import ABC, abstractmethod

import pygame

import src.app_config as cfg
from src.enums import Play
from src.controls import ARROW, WSAD
from src.game_states.game_state import GameState
from src.snake import Snake
import src.ui.ui_elements as ui
from src.utils import align_center_to_grid, get_rand_coord


class PlayState(GameState):

    def __init__(self, game, level_config):
        super().__init__(game)
        self.level_config = level_config
        
        self.border = None
        self.snakes = None
        self.fruits = None
        
        self.setup_border()
        self.setup_snakes()
        self.setup_fruit()

        self.commands = {
            Play.START: False, 
            Play.PAUSE: False,
            Play.QUIT: False
        }

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def setup_snakes(self):
        pass

    @abstractmethod
    def handle_fruit_collision(self, snake):
        pass


    def handle_event(self, event):

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.commands[Play.PAUSE] = True
            if event.key == pygame.K_ESCAPE:
                self.commands[Play.QUIT] = True

            for snake in self.snakes:
                snake.handle_event_keydown(event)

        keys = pygame.key.get_pressed()

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

    def setup_border(self):
        if self.level_config.has_border:
            self.border = ui.create_border(self.level_config.cell_size)
        else:
            self.border = None

    def setup_fruit(self):
        self.fruits = []
        self.add_fruit(self.level_config.fruit_qty)
          
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
        self.add_fruit(self.level_config.fruit_qty)