# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        current = head
        
        prev_node = ListNode(val = head.val)
        prev_node.next = None
        next_node = None

        traversal = head.next
        while traversal:
            current = traversal
            next_node = ListNode(val = current.val)
            next_node.next = prev_node
            prev_node = next_node
            traversal = traversal.next
        
        if next_node is not None:
            return next_node
        else:
            return prev_node

        return inverted_head