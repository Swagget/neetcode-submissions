# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        if root.left:
            to_return = self.inorderTraversal(root.left)
        else: 
            to_return = []
        to_return.append(root.val)
        
        if root.right:
            right_tree_in_order = self.inorderTraversal(root.right)
            for ele in right_tree_in_order:
                to_return.append(ele)
        return to_return