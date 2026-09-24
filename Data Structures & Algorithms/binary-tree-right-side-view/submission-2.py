# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        answers = []
        level = 0

        if root:
            queue.append(root)
        
        while len(queue) != 0:
            current_level_answer = None
            for ele in range(len(queue)):
                node = queue.popleft()
                current_level_answer = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if current_level_answer:
                answers.append(current_level_answer)
        return answers