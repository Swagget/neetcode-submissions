# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        list_of_lists = []
        queue = deque()

        if root:
            queue.append(root)
        
        while len(queue) != 0:
            temp = []
            for index in range(len(queue)):
                node = queue.popleft()
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            list_of_lists.append(temp)
        return list_of_lists