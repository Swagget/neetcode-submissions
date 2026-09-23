class MyStack:

    def __init__(self):
        self.main_queue = deque([])
        self.intermediate_queue = deque([])

    def push(self, x: int) -> None:
        self.main_queue.append(x)
        for _ in range(len(self.main_queue)-1):
            self.intermediate_queue.append(self.main_queue.popleft())
            self.main_queue.append(self.intermediate_queue.popleft())
        

    def pop(self) -> int:
        return self.main_queue.popleft()

    def top(self) -> int:
        return self.main_queue[0]

    def empty(self) -> bool:
        return len(self.main_queue) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()