import random
import time

import pygame

import config as cfg
from game_state import State
from snake import Snake
import ui_elements as ui


class Game:

    def __init__(self, window_size):
        self.window_w, self.window_h = self.window_size = window_size
        self.running = True
        self.game_state = State.TITLE
        self.players = 1
        self.run_state = None
        self.p1_score = 0
        self.p2_score = 0
        self.cell_size = 32
        self.display_size = (self.cell_size - 4, self.cell_size - 4)
        self.snakes = [Snake(window_size), Snake(window_size)]
        self.snake = Snake(window_size)
        self.snake2 = Snake(window_size)
        self.fruits = []
        self.add_fruit(4)
    
    def run(self, window):
        clock = pygame.time.Clock()
        while self.running:
            self.handle_events()
            self.update()
            self.draw(window)
            pygame.display.flip()
            clock.tick(120)

    def handle_events(self):
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            # self.game_state.handle_events(event)

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
                        print(self.snake.body)
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
        # self.game_state.update()
        if self.game_state == State.PLAYING:
            time_now = time.perf_counter()

            if self.players == 1:
                self.snake.update(time_now)
                if not self.snake.alive:
                    self.snake.reset()
                    self.p1_score = 0
                if self.check_hit_fruit(self.snake):
                    self.update_fruit(self.snake)
                    self.p1_score += len(self.snake.body) * 10
            
            if self.players == 2:
                if not self.snake.update(time_now):
                    self.snake.reset()
                    self.p1_score = 0
                if self.check_hit_fruit(self.snake):
                    self.update_fruit(self.snake)
                    self.p1_score = len(self.snake.body) * 10
                
                if not self.snake2.update(time_now):
                    self.snake2.reset()
                    self.p2_score = 0
                if self.check_hit_fruit(self.snake2):
                    self.update_fruit(self.snake2)
                    self.p2_score += len(self.snake2.body) * 10

                self.check_snake_collision(self.snake, self.snake2)
         
    def draw(self, window):
        window.fill(cfg.BACKGROUND_COLOR)

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
                    self.p1_score)
                window.blit(SCORE_BANNER_SURF, SCORE_BANNER_RECT)
            elif self.players == 2:
                SCORE_BANNER_SURF, SCORE_BANNER_RECT = ui.create_2player_score_banner(
                    self.p1_score, self.p2_score)
                window.blit(SCORE_BANNER_SURF, SCORE_BANNER_RECT)

            for fruit in self.fruits:
                pygame.draw.rect(
                    window, cfg.FRUIT_COLOR, ((fruit), (self.display_size))
                )

            self.snake.draw(window)
            if self.players == 2:
                self.snake2.draw(window)

            if self.game_state == State.START:
                window.blit(ui.PRESS_SPACE_SURF, ui.PRESS_SPACE_RECT)

    def change_state(self, state):
        self.game_state = state

    def set_run_state(self, state):
        self.run_state = state

    def change_cell_size(self, size):
        if self.window_w % size == 0:
            self.cell_size = size

    def set_players(self, num):
        self.players = num

    def setup_snakes(self, players):
        if players == 1:
            self.snake = Snake(
                self.window_size, self.cell_size, 
                (self.window_w // 2, self.window_h // 2),
                color=cfg.MAIN_COLOR
            )

        if players == 2:
            self.snake = Snake(
                self.window_size, self.cell_size, 
                (self.window_w * .75, self.window_h // 2), (-1, 0),
                color=cfg.MAIN_COLOR
            )
            self.snake2 = Snake(
                self.window_size, self.cell_size, 
                (self.window_w * .25, self.window_h // 2),
                color= cfg.PLAYER_TWO_COLOR
            )
         
    def update_fruit(self, snake):
        fruit_hit = self.check_hit_fruit(snake)
        if fruit_hit:
            snake.eat()
            self.remove_fruit(fruit_hit)
            self.add_fruit()
    
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
            rand_x = random.randint(0, (self.window_size[0] // self.cell_size) - 1)                          
            rand_y = random.randint(0, (self.window_size[1] // self.cell_size) - 1)
            if (
                (rand_x, rand_y) not in self.snake.body 
                and (rand_x, rand_y) not in self.snake2.body
            ):
                    self.fruits.append(
                        (rand_x * self.cell_size, rand_y * self.cell_size)
                    )
            else:
                self.add_fruit()
        
    def check_hit_fruit(self, snake):
        for fruit in self.fruits:
            if fruit == snake.head_position:
                return fruit
                            
    def remove_fruit(self, fruit):
        self.fruits.remove(fruit)
