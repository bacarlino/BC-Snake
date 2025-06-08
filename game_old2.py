import random
import time

import pygame

from config import *
from game_state import State
from menu import Menu
from snake import Snake
import ui_elements as ui


class Game:

    def __init__(self):
        self.running = True
        self.game_state = State.TITLE
        self.players = 1
        self.p1_score = 0
        self.p2_score = 0

        self.cell_size = 32
        self.display_size = (self.cell_size - 2, self.cell_size - 2)
        self.width, self.height  = pygame.display.get_window_size()
        self.rows = self.height // self.cell_size
        self.columns = self.width // self.cell_size
        
        self.snake = Snake()
        self.snake2 = Snake()

        self.fruits = []
        self.add_fruit(10)
    
    def run(self, window):
        clock = pygame.time.Clock()
        
        while self.running:
            
            self.handle_events()
            self.update()
            self.draw(window)

            pygame.display.flip()
            
            clock.tick(120)

    def handle_events(self):
        # self.state.handle_events()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        
            if event.type == pygame.KEYDOWN:

                if self.game_state == State.TITLE_PLAYERS:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        self.players = 1
                        ui.players_menu.down()
        
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        self.players = 2
                        ui.players_menu.up()
                    
                if event.key == pygame.K_SPACE:
                    
                    if self.game_state == State.TITLE:
                        self.game_state = State.TITLE_PLAYERS
                    
                    elif self.game_state == State.TITLE_PLAYERS:
                        self.game_state = State.START
                        self.setup_snakes(self.players)

                    elif self.game_state == State.START:
                        self.game_state = State.PLAYING
                    
                    elif self.game_state == State.PLAYING:
                        self.game_state = State.PAUSED
                    
                    elif self.game_state == State.PAUSED:
                        self.game_state = State.PLAYING
                    
                    elif self.game_state == State.LOSS:
                        self.game_state = State.START

                if event.key == pygame.K_ESCAPE:
                    self.game_state = State.TITLE
        
        keys = pygame.key.get_pressed()
        
        if State.PLAYING:
            if keys[pygame.K_UP]:
                self.snake.next_move = "up"
            elif keys[pygame.K_DOWN]:
                self.snake.next_move = "down"
            elif keys[pygame.K_LEFT]:
                self.snake.next_move = "left"
            
            elif keys[pygame.K_RIGHT]:
                self.snake.next_move = "right"
            
            if self.players == 2:

                if keys[pygame.K_w]:
                    self.snake2.next_move = "up"
                
                elif keys[pygame.K_s]:
                    self.snake2.next_move = "down"
                
                elif keys[pygame.K_a]:
                    self.snake2.next_move = "left"
                
                elif keys[pygame.K_d]:
                    self.snake2.next_move = "right"
        
    def update(self):
        if self.game_state == State.PLAYING:

            time_now = time.perf_counter()

            if self.players == 1:
                self.update_snake(self.snake, time_now)
            if self.players == 2:
                self.update_snake(self.snake, time_now)
                self.update_snake(self.snake2, time_now)
                self.check_snake_collision(self.snake, self.snake2)
         

    def draw(self, window):
        window.fill(BACKGROUND_COLOR)

        if self.game_state == State.TITLE:
            window.blit(ui.PING_PANG_SURF, ui.PING_PANG_RECT)
            window.blit(ui.TITLE_SURF, ui.TITLE_RECT)
            window.blit(ui.PRESS_SPACE_SURF, ui.PRESS_SPACE_RECT)

        elif self.game_state == State.TITLE_PLAYERS:
            window.blit(ui.PING_PANG_SURF, ui.PING_PANG_RECT)
            window.blit(ui.TITLE_SURF, ui.TITLE_RECT) 
            ui.players_menu.draw(window)
            window.blit(ui.PRESS_SPACE_SURF, ui.PRESS_SPACE_RECT)

        else:
            if self.players == 1:
                SCORE_BANNER_SURF, SCORE_BANNER_RECT = ui.create_score_banner(
                    self.snake.score)
                window.blit(SCORE_BANNER_SURF, SCORE_BANNER_RECT)
            elif self.players == 2:
                SCORE_BANNER_SURF, SCORE_BANNER_RECT = ui.create_2player_score_banner(
                    self.snake.score, self.snake2.score)
                window.blit(SCORE_BANNER_SURF, SCORE_BANNER_RECT)


            # FRUIT
            for fruit in self.fruits:
                fruit = self.grid_to_pixel(fruit)
                pygame.draw.rect(
                    window, FRUIT_COLOR, ((fruit), (self.display_size))
                )

            # SNAKE
            for segment in self.snake.body:
                segment = self.grid_to_pixel(segment)    
                pygame.draw.rect(
                    window, MAIN_COLOR, ((segment), (self.display_size))
                )

            if self.players == 2:
                for segment in self.snake2.body:
                    segment = self.grid_to_pixel(segment)    
                    pygame.draw.rect(
                        window, PLAYER_TWO_COLOR, ((segment), (self.display_size))
                    )

            if self.game_state == State.START:
                window.blit(ui.PRESS_SPACE_SURF, ui.PRESS_SPACE_RECT)

    def change_state(self, state):
        self.game_state = state

    def set_players(self, num):
        self.players = num

    def grid_to_pixel(self, grid_position):
        return (
            grid_position[0] * self.cell_size, 
            grid_position[1] * self.cell_size
        )
    
    def setup_snakes(self, players):
        if players == 1:
            self.snake = Snake((self.columns // 2, self.rows // 2))

        if players == 2:
            self.snake = Snake((self.columns * .75, self.rows // 2), (-1, 0))
            self.snake2 = Snake((self.columns * .25, self.rows // 2))

    def update_snake(self, snake, time_now):
            snake_dt = time_now - snake.prev_time

            if snake_dt >= snake.timer:
                new_x, new_y = snake.update()

                if snake.body_collision(new_x, new_y):
                    snake.reset()
                    self.snake.score = 0
                    return
                
                new_x, new_y = self.check_wrap(snake, new_x, new_y)
                snake.set_head_position((new_x, new_y))
                snake.body.insert(0, snake.head_position)

                fruit_hit = self.check_hit_fruit(snake)
                if fruit_hit:
                    self.remove_fruit(fruit_hit)
                    snake.score += len(snake.body) * 15 
                    snake.timer /= snake.timer_reducer
                    self.add_fruit()
                else:
                    snake.body.pop(-1)

                snake.set_time(time_now)

    def check_snake_collision(self, snake, snake2):
        if snake.head_position == snake2.head_position:
            self.game_state = State.START
            snake.reset()
            snake2.reset()

        if snake.head_position in snake2.body:
            self.game_state = State.START
            snake.reset()

        if snake2.head_position in snake.body:
            self.game_state = State.START
            snake2.reset()

    
    def add_fruit(self, n=1):
        for _ in range(n):
            rand_x = random.randint(0, self.columns - 1)                          
            rand_y = random.randint(0, self.rows - 1)
            if (
                (rand_x, rand_y) not in self.snake.body 
                and (rand_x, rand_y) not in self.snake.body
            ):
                    self.fruits.append((rand_x, rand_y))
            else:
                self.add_fruit()
        
    def check_hit_fruit(self, snake):
        """Returns true if head_position is in the list of fruits"""
        for fruit in self.fruits:
            if fruit == snake.head_position:
                return fruit
                
            
    def remove_fruit(self, fruit):
        self.fruits.remove(fruit)

    # GRID
    def check_wrap(self, snake, x, y):
        if snake.head_position[0] >= self.columns:
            return (0, y)
        elif snake.head_position[0] < 0: 
            return (self.columns - 1, y)
        elif snake.head_position[1] >= self.rows:
            return (x, 0)
        elif snake.head_position[1] < 0:
            return (x, self.rows - 1)
        return (x, y)
