# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        return self.dfs(root,k)[0]
        
    def dfs(self, root, k): # Returns the (value/-1, new_k)
        if root is None:
            return [None, k]
        new_k = k
        if root.left:
            ans, new_k = self.dfs(root.left, k)
            if new_k == 0:
                return [ans, 0]
        if new_k == 1: 
            return [root.val, 0]
        new_k -= 1
        if root.right:
            ans, new_k = self.dfs(root.right, new_k)
            if new_k == 0:
                return [ans, 0]
        return [-1, new_k]