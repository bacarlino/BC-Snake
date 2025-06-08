import random
import sys
import time

import pygame


class Game:

    def __init__(self):
        self.running = True
        
        self.prev_time = time.perf_counter()

        # GRID
        self.cell_size = 32
        self.display_size = (self.cell_size - 2, self.cell_size - 2)
        self.width, self.height  = pygame.display.get_window_size()
        self.rows = self.height // self.cell_size
        self.columns = self.width // self.cell_size
        
        # SNAKE
        self.snake = []
        self.snake_grid_pos = (0, 0)
        self.direction = (0, 0)
        self.moving = False
        self.start_delay = .15
        self.delay = self.start_delay
        self.delay_decrease = 1.01
        self.create_snake()

        # FRUIT
        self.fruits = []
        self.add_fruit(2)
    
    def run(self, window):
        clock = pygame.time.Clock()

        while self.running:

            time_now = time.perf_counter()
            snake1_dt = time_now - self.prev_time
            
            self.handle_events()

            if snake1_dt >= self.delay:
                self.update()
                self.prev_time = time_now                
            
            self.draw(window)
            pygame.display.flip()
            clock.tick(120)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pass

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            if not self.direction[1]:
                self.direction = (0, -1)
                self.moving = True
        elif keys[pygame.K_DOWN]:
            if not self.direction[1]:
                self.direction = (0, 1)
                self.moving = True
        elif keys[pygame.K_LEFT]:
            if not self.direction[0]:
                self.direction = (-1, 0)
                self.moving = True
        elif keys[pygame.K_RIGHT]:
            if not self.direction[0]:
                self.direction = (1, 0)
                self.moving = True

    def update(self):
        new_x = self.snake_grid_pos[0] + (self.direction[0])
        new_y = self.snake_grid_pos[1] + (self.direction[1])
        
        new_x, new_y = self.check_wrap(new_x, new_y)
        self.snake_grid_pos = (new_x, new_y)

        

        if self.check_snake_collision(new_x, new_y):
            self.moving = False
            self.reset()
            return
        self.snake.insert(0, self.snake_grid_pos)

        # FRUIT
        if self.moving:
            print("Snake is moving")
            if not self.fruit_collision():
                print("No fruit collision")
                self.snake.pop(-1)
                print("snake should have popped")
            else:
                self.add_fruit()      

    def draw(self, window):
        window.fill((0, 0, 0))

        # FRUIT
        for fruit in self.fruits:
            fruit = self.grid_to_pixel(fruit)
            pygame.draw.rect(
                window, (0, 235, 100), ((fruit), (self.display_size))
            )

        # SNAKE
        for segment in self.snake:
            segment = self.grid_to_pixel(segment)    
            pygame.draw.rect(
                window, (235, 0, 100), ((segment), (self.display_size))
            )

    def grid_to_pixel(self, grid_position):
        return (
            grid_position[0] * self.cell_size, 
            grid_position[1] * self.cell_size
        )

    #SNAKE
    def create_snake(self):
        self.snake_grid_pos = self.columns // 2, self.rows // 2
        for count in range(5):
            self.snake.append(
                (self.columns // 2 - (1 * count), self.rows // 2)
            )

    def add_fruit(self, n=1):
        for _ in range(n):
            rand_x = random.randint(0, self.columns - 1)                          
            rand_y = random.randint(0, self.rows - 1)
            if (rand_x, rand_y) not in self.snake:
                self.fruits.append((rand_x, rand_y))
            else:
                print("Food tried to spawn inside of snake", (rand_x, rand_y), self.snake)
                self.add_fruit()
        
    def fruit_collision(self):
        for fruit in self.fruits:
            if fruit == self.snake_grid_pos:
                self.remove_fruit(fruit)
                self.delay /= self.delay_decrease
                print(self.delay)
                return True
            
    def remove_fruit(self, fruit):
        self.fruits.remove(fruit)

    def check_wrap(self, x, y):
        if self.snake_grid_pos[0] >= self.columns:
            return (0, y)
        elif self.snake_grid_pos[0] < 0: 
            return (self.columns - 1, y)
        elif self.snake_grid_pos[1] >= self.rows:
            return (x, 0)
        elif self.snake_grid_pos[1] < 0:
            return (x, self.rows - 1)
        return (x, y)

    def check_snake_collision(self, x, y):
        if (x, y) in self.snake[4:]:
            print("snake_collision")
            print("grid_pos, full_snake")
            print(self.snake_grid_pos, self.snake)
            return True

    # SNAKE
    def reset(self):
        print("reset")
        self.snake = []
        self.create_snake()
        self.direction = (0, 0)
        self.delay = self.start_delay