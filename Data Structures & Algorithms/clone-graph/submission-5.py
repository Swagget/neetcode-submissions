"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        fully_written = set()
        copy_value_generated = {} # If the node of the value was generated in the copy graph, then this will point value -> Node
        root_copy = Node()
        copy_queue = deque()
        queue = deque()
        queue.append(node)
        copy_queue.append(root_copy)
        copy_value_generated[node.val] = root_copy
        while len(queue) > 0:
            current_queue_len = len(queue)
            for _ in range(current_queue_len):
                node_to_copy = queue.popleft()
                node_being_written = copy_queue.popleft()
                node_being_written.val = node_to_copy.val
                fully_written.add(node_to_copy)
                for neighbor in node_to_copy.neighbors:
                    if neighbor.val not in copy_value_generated: # This means it needs to be created for the first time    
                        new_node = Node()
                        copy_value_generated[neighbor.val] = new_node
                        queue.append(neighbor)
                        copy_queue.append(new_node)
                    node_being_written.neighbors.append(copy_value_generated[neighbor.val])
        return root_copy