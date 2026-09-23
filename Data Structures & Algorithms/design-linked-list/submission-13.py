class Node:
    def __init__(self, val = -1, next_node = None, prev_node = None):
        self.val = val
        self.next_node = next_node
        self.prev_node = prev_node

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.length:
            return -1
        temp = self.head
        for i in range(index):
            temp = temp.next_node
        return temp.val

    def addAtHead(self, val: int) -> None:
        if self.length == 0:
            self.head = self.tail = Node(val = val)
            self.length += 1
        else:
            new_node = Node(val = val, next_node = self.head)
            self.head.prev_node = new_node
            self.head = new_node
            self.length += 1

    def addAtTail(self, val: int) -> None:
        if self.length == 0:
            self.head = self.tail = Node(val = val)
            self.length += 1
        else:
            new_node = Node(val = val, prev_node = self.tail)
            self.tail.next_node = new_node
            self.tail = new_node
            self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.length:
            return None
        if index == 0:
            self.addAtHead(val)
        elif index == self.length:
            self.addAtTail(val)
        else:
            temp = self.head
            for i in range(index - 1):
                temp = temp.next_node
            new_node = Node(val = val, prev_node = temp, next_node = temp.next_node)
            temp.next_node.prev_node = new_node
            temp.next_node = new_node
            self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.length:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
        elif index == 0:
            self.head = self.head.next_node
            self.head.prev_node = None
        elif index == self.length - 1:
            self.tail = self.tail.prev_node
            self.tail.next_node = None
        else:
            temp = self.head
            for i in range(index - 1):
                temp = temp.next_node
            temp.next_node = temp.next_node.next_node
            temp.next_node.prev_node = temp
        self.length -= 1
