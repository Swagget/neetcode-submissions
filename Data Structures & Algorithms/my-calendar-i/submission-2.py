class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None
    
    def insert(self, start, end):
        current = self
        while True:
            if start >= current.end:
                if current.right is None:
                    current.right = Node(start = start, end = end)
                    return True
                current = current.right
            elif end <= current.start:
                if current.left is None:
                    current.left = Node(start = start, end = end)
                    return True
                current = current.left
            else:
                return False

class MyCalendar:
    
    def __init__(self):
        self.root = None

    def book(self, startTime: int, endTime: int) -> bool:
        if not self.root:
            self.root = Node(start = startTime, end = endTime)
            return True
        return self.root.insert(startTime, endTime)


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)