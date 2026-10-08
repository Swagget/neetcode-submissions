# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Print current node.
        # Add right to stack. 
        # Move left.
        if root is None:
            return []

        stack = [root]
        current = None
        to_return = []

        while len(stack) > 0:
            current = stack.pop()
            to_return.append(current.val)
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
        return to_return