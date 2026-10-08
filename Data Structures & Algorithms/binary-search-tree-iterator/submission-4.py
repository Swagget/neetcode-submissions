# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.current = root
        self.stack = deque()

    def next(self) -> int:
        while True:
            if self.current:
                self.stack.append(self.current)
                self.current = self.current.left
            else:
                self.current = self.stack.pop()
                val = self.current.val
                self.current = self.current.right
                return val


    def hasNext(self) -> bool:
        if self.current or len(self.stack) > 0:
            return True
        return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()