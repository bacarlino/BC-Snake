import time

import pygame

from src.ui.border import Border
from src.ui.ui_config import BORDER_RADIUS, GREEN
from src.enums import Play
from src.factories import create_one_player_snakes
from src.game_states.game_state import GameState
from src.ui.ui_config import PINK, PURPLE
from src.ui.ui_elements import ScoreBanner
from src.utils import get_rand_coord


class PlayState(GameState):
    """Single player mode"""

    def __init__(self, game, level_config):
        super().__init__(game)
        
        self.level_config = level_config
        self.match_over = False
        
        self.border = None
        self.setup_border()
        
        self.snakes = None
        self.setup_snakes()
        self.set_snakes_moving()
        
        self.fruits = []
        self.add_fruit(self.level_config.fruit_qty)

        self.score_banner = ScoreBanner(str(self.snakes[0].score))

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
        print("snake.score: ", self.snakes[0].score)
        self.score_banner.update(self.snakes[0].score)
        self.reset_command_flags()

    def draw(self, window):
        if self.border:
            self.border.draw(window)
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
            self.border.draw(window)

    def draw_score(self, window):
        self.score_banner.draw(window)

    def draw_fruit(self, window):
        for fruit in self.fruits:
            pygame.draw.rect(
                window, GREEN, ((fruit), (self.game.display_size)), border_radius=BORDER_RADIUS
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
            self.border = Border(self.game.window_size, self.level_config.cell_size, self.level_config.border_color)
        else:
            self.border = None

    def setup_fruit(self):
        self.add_fruit(self.level_config.fruit_qty)
          
    def add_fruit(self, n=1):
        for _ in range(n):
            placed = False
            while not placed:
                coord = get_rand_coord(
                    self.game.window_size, self.level_config.cell_size
                )
                if self.border and coord in self.border.coord_list: continue
               
                if coord in self.snake_segment_list(): 
                    continue

                placed = True
                self.fruits.append(coord)

    def snake_segment_list(self):
        return [segment for snake in self.snakes for segment in snake.body]

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