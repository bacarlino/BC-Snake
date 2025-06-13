import time

import pygame

import src.config as cfg
from src.game_states.game_over import GameOver
from src.game_states.game_state import GameState
from src.input import Play
from src.game_states.pause import Pause
from src.snake import Snake
import src.ui_elements as ui


class RunTwoPlayer(GameState):

    def __init__(self, game):
        super().__init__(game)

        self.game.clear_snakes()
        self.game.add_snake(
            Snake(
                self.game.window_size, self.game.cell_size, 
                (self.game.window_w * .75, (self.game.window_h // 2) - self.game.cell_size), (0, 1),
                color=cfg.PINK
            )
        )

        self.game.add_snake(
            Snake(
                self.game.window_size, self.game.cell_size, 
                (self.game.window_w * .25, self.game.window_h // 2), (0, -1),
                color=cfg.PURPLE
            )
        )

        self.border = ui.create_border(self.game.cell_size)

        self.headon_collision = False

        self.inputs = {
            Play.SNAKE_ONE_UP: False,
            Play.SNAKE_ONE_DOWN: False,
            Play.SNAKE_ONE_LEFT: False,
            Play.SNAKE_ONE_RIGHT: False,
            Play.SNAKE_TWO_UP: False,
            Play.SNAKE_TWO_DOWN: False,
            Play.SNAKE_TWO_LEFT: False,
            Play.SNAKE_TWO_RIGHT: False,
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
        elif keys[pygame.K_w]:
            self.inputs[Play.SNAKE_TWO_UP] = True
        elif keys[pygame.K_s]:
            self.inputs[Play.SNAKE_TWO_DOWN] = True
        elif keys[pygame.K_a]:
            self.inputs[Play.SNAKE_TWO_LEFT] = True
        elif keys[pygame.K_d]:
            self.inputs[Play.SNAKE_TWO_RIGHT] = True

    def update(self):
        time_now = time.perf_counter()

        if self.inputs[Play.PAUSE] == True:
            self.game.change_state(Pause(self.game))
        if self.inputs[Play.QUIT] == True:
            self.game.reset_game()
            return

        if self.inputs[Play.SNAKE_ONE_UP]:
            self.game.snakes[0].next_direction = "up"
        if self.inputs[Play.SNAKE_ONE_DOWN]:
            self.game.snakes[0].next_direction = "down"
        if self.inputs[Play.SNAKE_ONE_LEFT]:
            self.game.snakes[0].next_direction = "left"
        if self.inputs[Play.SNAKE_ONE_RIGHT]:
            self.game.snakes[0].next_direction = "right"
        
        if self.inputs[Play.SNAKE_TWO_UP]:
            self.game.snakes[1].next_direction = "up"
        if self.inputs[Play.SNAKE_TWO_DOWN]:
            self.game.snakes[1].next_direction = "down"
        if self.inputs[Play.SNAKE_TWO_LEFT]:
            self.game.snakes[1].next_direction = "left"
        if self.inputs[Play.SNAKE_TWO_RIGHT]:
            self.game.snakes[1].next_direction = "right"

        self.game.snakes[0].update(time_now, self.border, self.game.snakes[1])
        self.game.snakes[1].update(time_now, self.border, self.game.snakes[0])

        for index, snake in enumerate(self.game.snakes):
            self.game.update_fruit(snake, index)
            if snake.collide:
                snake.die()
                self.game.change_state(GameOver(self.game))
            
        self.game.check_snake_collision()

        self.reset_inputs()

    def draw(self, window):
        SCORE_BANNER_SURF, SCORE_BANNER_RECT = ui.create_2player_score_banner(
            self.game.scores[0], self.game.scores[1]
        )
        window.blit(SCORE_BANNER_SURF, SCORE_BANNER_RECT)

        for fruit in self.game.fruits:
            pygame.draw.rect(
                window, cfg.LIME, ((fruit), (self.game.display_size))
            )

        ui.draw_border(window, self.border, self.game.cell_size)

        for snake in self.game.snakes:
            snake.draw(window)
        
        # self.snake.draw(window)

    def check_snake_collision(self):
        snake = self.snakes[0]
        snake2 = self.snakes[1]

        if snake.head_position == snake2.head_position:
            snake.die()
            snake2.die()
            self.game_state = GameOver(self)

        if snake.head_position in snake2.body:
            snake.die()
            self.game_state = GameOver(self)

        if snake2.head_position in snake.body:
            snake2.die()
            self.game_state = GameOver(self)