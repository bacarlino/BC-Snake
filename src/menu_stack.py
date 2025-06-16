class MenuStack:

    def __init__(self):
        self.stack = []

    def push(self, menu):
        self.stack.append(menu)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def handle_events(self):
        self.stack[-1].handle_events()

    def update(self):
        self.stack[-1].update()

    def draw(self, window):
        self.stack[-1].draw()