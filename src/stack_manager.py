class StackManager:

    def __init__(self):
        self.stack = []

    def push(self, state):
        self.stack.append(state)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]
    
    def peek_below(self):
        return self.stack[-2]
    
    def handle_events(self, event):
        self.peek().handle_events(event)

    def update(self):
        self.peek().update()
        
    def draw(self, window):
        self.peek().draw(window)