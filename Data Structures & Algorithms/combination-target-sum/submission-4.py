class Nodes:
    def __init__(self, target_left= -1, path = [], available_nums = []):
        self.target_left = target_left
        self.path = path
        self.available_nums = available_nums
        self.children = []
        self.expanded = False
    
    def expand_node(self):
        self.expanded = True
        new_children_to_expand = []
        successful_paths = []
        for ele in self.available_nums:
            returned = self.add_node(ele)
            if returned.target_left > 0:
                new_children_to_expand.append(returned)
            elif returned.target_left == 0:
                successful_paths.append(returned.path)

        return (new_children_to_expand, successful_paths)

    
    def add_node(self, ele):
        new_target_left = self.target_left - ele
        new_path = self.path + [ele]
        new_node = Nodes(target_left = new_target_left, path = new_path)
        new_available_nums = []
        for ele_2 in self.available_nums:
            if ele_2 <= new_target_left and ele_2 >= ele:
                new_available_nums.append(ele_2)
        new_node.available_nums = new_available_nums
        self.children.append(new_node)
        return new_node

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        queue = deque()
        root_node = Nodes(target_left = target, path = [], available_nums = nums)
        queue.append(root_node)
        to_return = []

        while len(queue) != 0:
            node_to_expand = queue.popleft()
            new_children, successful_paths = node_to_expand.expand_node()
            for ele in new_children:
                queue.append(ele)
            for ele in successful_paths:
                to_return.append(ele)
        return to_return