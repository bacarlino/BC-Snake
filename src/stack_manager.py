class StackManager:

    def __init__(self):
        self.stack = []

    def push(self, item):
        print(f"Push to: {self.stack}")
        self.stack.append(item)

    def pop(self):
        print(f"Pop from: {self.stack}")
        if self.stack:
            return self.stack.pop()

    def peek(self):
        print(f"Peek from: {self.stack}")
        if self.stack:
            return self.stack[-1]
    
    def peek_below(self):
        if self.stack:
            return self.stack[-2]
    
    def handle_events(self, event):
        if self.stack:
            self.peek().handle_events(event)

    def update(self):
        if self.stack:
            self.peek().update()
        
    def draw(self, window):
        if self.stack:
            self.peek().draw(window)