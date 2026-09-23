# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        actual_head = head
        if head is None:
            return None
        else:
            temp = head.next
            if not temp is None:
                actual_head = self.reverseList(temp)
                temp.next = head
        head.next = None
        return actual_head