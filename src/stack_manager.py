class StackManager:

    def __init__(self):
        self.stack = []

    def handle_event(self, event):
        if self.stack:
            self.peek().handle_event(event)

    def update(self):
        if self.stack:
            self.peek().update()
        
    def draw(self, window):
        if self.stack:
            self.peek().draw(window)

    def push(self, item):
        self.stack.append(item)
   
    def pop(self):
        if self.stack:
            return self.stack.pop()
        
    def clear(self):
        self.stack.clear()
    
    def peek(self):
        if self.stack:
            return self.stack[-1]
    
    def peek_below(self):
        if self.stack:
            return self.stack[-2]   
    
    def transition_to(self, state):
        self.pop()
        self.push(state)

    def has_one_item(self):
        return True if len(self.stack) == 1 else False  