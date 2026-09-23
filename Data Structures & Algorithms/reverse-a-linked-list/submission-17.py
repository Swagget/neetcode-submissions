# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None: # This isn't base case, it's just edge case
            return None
        if head.next is None:
            return head
        actual_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return actual_head