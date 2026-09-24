# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def height(self, node) -> int:
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        return 1+max(self.height(node.left), self.height(node.right))
        


    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        left_height = self.height(root.left)
        right_height = self.height(root.right)

        
        if abs(right_height - left_height) > 1: # takes care of the base case
            return False
        if not self.isBalanced(root.left):
            return False
        if not self.isBalanced(root.right):
            return False
        return True
        