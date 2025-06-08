import time

class Snake:

    def __init__(self, position=(0, 0), velocity=(1, 0)):
        self.body = []
        self.initial_position = position
        self.head_position = self.initial_position
        self.initial_velocity = velocity
        self.velocity = self.initial_velocity
        self.next_move = None
        self.initial_timer = .15
        self.timer = self.initial_timer
        self.timer_reducer = 1.05
        self.prev_time = time.perf_counter()
        self.score = 0
        self.fill_body()

    def fill_body(self, length=5):
        for count in range(length):
            self.body.append(
                (
                    self.head_position[0] - self.velocity[0] * count, 
                    self.head_position[1] - self.velocity[1] * count
                )
            )

    def reset(self):
        self.moving = False
        self.head_position = self.initial_position
        self.velocity = self.initial_velocity
        self.timer = self.initial_timer
        self.body = []
        self.fill_body()
    

    def update(self):
        self.set_velocity()
        new_x = self.head_position[0] + (self.velocity[0])
        new_y = self.head_position[1] + (self.velocity[1])
        return (new_x, new_y)
    
    def set_time(self, time_now):
        self.prev_time = time_now
    
    def set_head_position(self, position):
        self.head_position = position

    def body_collision(self, x, y):
        if (x, y) in self.body[3:]:
            return True
        return False
  
    def set_velocity(self, cell_size=1):
        if self.next_move == "up":
            if not abs(self.velocity[1]):
                self.velocity = (0, -cell_size)
        elif self.next_move == "down":
            if not abs(self.velocity[1]):
                self.velocity = (0, cell_size)
        elif self.next_move == "left":
            if not abs(self.velocity[0]):
                self.velocity = (-cell_size, 0)
        elif self.next_move == "right":
            if not abs(self.velocity[0]):
                self.velocity = (cell_size, 0)