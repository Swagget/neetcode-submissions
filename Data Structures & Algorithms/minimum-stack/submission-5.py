class MinStack:

    def __init__(self):
        self.stack = []
        self.top_index = -1
        self.minimum_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.top_index += 1
        if len(self.minimum_stack) == 0:
            self.minimum_stack.append(val)
        else:
            self.minimum_stack.append(min(self.minimum_stack[-1], val))

    def pop(self) -> None:
        to_return = self.stack[-1]
        del self.stack[self.top_index]
        del self.minimum_stack[self.top_index]
        self.top_index -= 1
        return to_return

    def top(self) -> int:
        return self.stack[self.top_index]

    def getMin(self) -> int:
        return self.minimum_stack[self.top_index]
        
