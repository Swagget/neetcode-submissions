# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.cnt = k
        self.res = root.val

        self.dfs(root)

        return self.res
        
    def dfs(self, node):
        if not node:
            return

        self.dfs(node.left)
        if self.cnt == 0:
            return
        self.cnt -= 1
        if self.cnt == 0:
            self.res = node.val
            return
        self.dfs(node.right)