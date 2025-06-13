class StateManager:

    def __init__(self):
        self.stack = []

    def push(self, state):
        self.stack.append(state)
        print(f"Pushed {state} on the stack: ")
        for item in self.stack:
            print(item)
        print()

    def pop(self):
        print(f"Popping {self.stack[-1]}: ")
        for item in self.stack:
            print(item)
        print()
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