import time

import pygame

import src.app_config as cfg
from src.enums import Play
from src.factories import create_one_player_snakes
from src.game_states.game_state import GameState
import src.ui.ui_elements as ui
from src.utils import get_rand_coord


class PlayState(GameState):
    """Single player mode"""

    def __init__(self, game, level_config):
        super().__init__(game)
        self.level_config = level_config
        self.match_over = False
        
        self.border = None
        self.snakes = None
        self.fruits = None
        
        self.setup_border()
        self.setup_snakes()
        self.set_snakes_moving()
        self.setup_fruit()

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

    def update(self):
        if self.update_commands(): return
        self.update_snakes()
        self.reset_command_flags()

    def draw(self, window):
        self.draw_border(window)
        self.draw_fruit(window)
        self.draw_snakes(window)
        self.draw_score(window)

    def update_commands(self):
        if self.commands[Play.PAUSE]:
            self.game.push_pause()
        if self.commands[Play.QUIT]:
            self.game.reset_game()
            return True
        return False
    
    def update_snakes(self):
        time_now = time.perf_counter()
        self.match_over = False

        for snake in self.snakes:
            other_snakes = self.other_snakes(snake)
            snake.update(time_now, self.border, other_snakes)
            self.handle_snake_collision(snake)
            self.handle_fruit_collision(snake)

        self.check_game_over()

    def other_snakes(self, snake):
        return [
            other for other in self.snakes if other is not snake
        ]
    
    def handle_snake_collision(self, snake):
        for snake in self.snakes:
            if snake.collision_detected:
                snake.die()
                self.match_over = True

    def check_game_over(self):
        if self.match_over:
            self.game.push_game_over()

    def draw_border(self, window):
        if self.level_config.has_border:
            ui.draw_border(window, self.border, self.level_config.cell_size)

    def draw_score(self, window):
        score_surf, score_rect = ui.create_score_banner(
            self.snakes[0].score
        )
        window.blit(score_surf, score_rect)

    def draw_fruit(self, window):
        for fruit in self.fruits:
            pygame.draw.rect(
                window, cfg.GREEN, ((fruit), (self.game.display_size)), border_radius=cfg.BORDER_RADIUS
            )

    def draw_snakes(self, window):
        for snake in self.snakes:
            snake.draw(window)

    def setup_snakes(self):
        self.snakes = create_one_player_snakes(self.game.window_size, self.level_config)
        
    def set_snakes_moving(self):
        for snake in self.snakes:
            snake.moving = True

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
               
                snake_segments = [
                    segment for snake in self.snakes for segment in snake.body
                ]
                if coord in snake_segments: 
                    print("COORD IN SNAKE_SEGMENT, CONTINUE")
                    continue

                placed = True
                self.fruits.append(coord)

    def handle_fruit_collision(self, snake):
        if snake.head_position in self.fruits:
            snake.eat(self.level_config.growth_rate)
            snake.score += (len(snake.body) * 10)
            self.fruits.remove(snake.head_position)
            self.add_fruit()

    def reset_run_state(self):
        for snake in self.snakes:
            snake.reset()
        self.fruits = []
        self.add_fruit(self.level_config.fruit_qty)