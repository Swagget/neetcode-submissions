# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        hash_set = {} # index -> value
        slow = head
        fast = head.next
        i = 0
        hash_set[i] = slow.val
        n = 0
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            i += 1
            hash_set[i] = slow.val
            n += 2
        i = 0
        max_value = 0
        slow = slow.next
        while slow is not None: # Check current twin
            twin_index = (n/2) - i
            max_value = max(max_value, slow.val + hash_set[twin_index])
            i += 1
            slow = slow.next
        return max_value