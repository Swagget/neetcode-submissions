# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Post order
        if root is None:
            return []
        stack = [root]
        to_traverse = [True]

        to_return = []

        while len(stack) > 0:
            current = stack.pop()# What happens if I pop from an empty stack? Error
            traverse = to_traverse.pop()
            if traverse == False:
                to_return.append(current.val)
                continue
            else:
                stack.append(current)
                to_traverse.append(False)
                if current.right:
                    stack.append(current.right)
                    to_traverse.append(True)
                if current.left:
                    stack.append(current.left)
                    to_traverse.append(True)

        return to_return