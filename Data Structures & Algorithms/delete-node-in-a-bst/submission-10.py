# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if root.val > key:
            root.left = self.deleteNode(root.left, key = key)
            return root
        elif root.val < key:
            root.right = self.deleteNode(root.right, key = key)
            return root
        else:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            else:
                min_of_right = self.find_min(root.right)
                root.val = min_of_right
                root.right = self.deleteNode(root = root.right, key = min_of_right)
                return root
    def find_min(self, root):
        while root.left:
            return self.find_min(root.left)
        return root.val