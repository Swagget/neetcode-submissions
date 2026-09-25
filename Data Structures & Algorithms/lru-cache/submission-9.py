class Node:
    def __init__(self, key, next_node = None, prev_node = None):
        self.key = key
        self.next_node = next_node
        self.prev_node = prev_node

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}# store value and node as a list here.
        self.head_node = None
        self.tail_node = None

    def get(self, key: int) -> int:
        if key in self.cache:
            self.reset_arbit(self.cache[key][1])
            return self.cache[key][0]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key][0] = value
            self.reset_arbit(self.cache[key][1])
        elif len(self.cache) == self.capacity:
            temp_key = self.pop_tail()
            del self.cache[temp_key]
            self.push_head(key)
            self.cache[key] = [value, self.head_node]
        else:
            self.push_head(key)
            self.cache[key] = [value, self.head_node]

    
    def pop_tail(self): # keeps track of the node, deletes it from the cache
        if self.tail_node == self.head_node:
            temp = self.tail_node
            temp_val = temp.key
            self.tail_node = None
            self.head_node = None
            return temp_val
        temp = self.tail_node
        temp_val = temp.key
        self.tail_node = self.tail_node.prev_node
        self.tail_node.next_node = None
        del temp
        return temp_val

    def push_head(self, key):
        if self.head_node is None:
            new_node = Node(key = key)
            self.head_node = new_node
            self.tail_node = new_node
        else:
            new_node = Node(key = key)
            new_node.next_node = self.head_node
            self.head_node.prev_node = new_node
            self.head_node = new_node
    
    def reset_arbit(self, arbit_node): # Remove it from queue and put it in head
    # Keep a track of capacity and current usage is 1 then deal with it. 
    # Then these other cases happen. 
        if self.head_node is self.tail_node:
            return
        if arbit_node is self.head_node:
            return
        if arbit_node is self.tail_node:
            new_tail = self.tail_node.prev_node
            new_tail.next_node = None
            self.tail_node.next_node = self.head_node
            self.head_node.prev_node = self.tail_node
            self.head_node = self.tail_node
            self.tail_node = new_tail
            self.head_node.prev_node = None
        else:
            arbit_node.next_node.prev_node = arbit_node.prev_node
            arbit_node.prev_node.next_node = arbit_node.next_node
            arbit_node.next_node = self.head_node
            self.head_node.prev_node = arbit_node
            self.head_node = arbit_node
            self.head_node.prev_node = None