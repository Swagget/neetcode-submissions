# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.preorder = preorder
        self.inorder = inorder
        self.inorder_hash = {value:index for index, value in enumerate(inorder)}
        self.preorder_index = 0
        return self.tree_constructor(0, len(inorder)-1)
        
    def tree_constructor(self, inorder_beginning, inorder_end) -> Optional[TreeNode]: # These indices are inclusive both sides. Number of elements in this subtree is end - beginning. If 0 we should stop
        if len(self.preorder) <= self.preorder_index or inorder_end < inorder_beginning:
            return None
        root_val = self.preorder[self.preorder_index]
        root = TreeNode(val = root_val)
        self.preorder_index += 1

        mid = self.inorder_hash[root_val]
        left_subtree_beginning = inorder_beginning
        # double check this. Slicing includes start but not stop. Index returns the index of first occurance, second parameter tells it where it is allowed to begin searching, default is = 0.
        right_subtree_beginning = mid + 1
        left_subtree_end = mid - 1
        right_subtree_end = inorder_end

        root.left = None
        root.right = None
        if left_subtree_end - left_subtree_beginning >= 0:
            root.left = self.tree_constructor(inorder_beginning = left_subtree_beginning, inorder_end = left_subtree_end)
        if right_subtree_end - right_subtree_beginning >= 0:
            root.right = self.tree_constructor(inorder_beginning = right_subtree_beginning, inorder_end = right_subtree_end)
        
        return root