# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        to_return_head = ListNode(l1.val + l2.val)
        tail = to_return_head
        carry_over = False
        if l1.val + l2.val >= 10:
            carry_over = True
            to_return_head.val = to_return_head.val%10
        l1 = l1.next
        l2 = l2.next

        while l1 or l2 or carry_over:
            new_temp = 0
            if l1:
                new_temp += l1.val
                l1 = l1.next
            if l2:
                new_temp += l2.val
                l2 = l2.next
            if carry_over:
                new_temp += 1
            if new_temp >= 10:
                carry_over = True
                new_temp = new_temp%10
            else: carry_over = False

            new_node = ListNode(new_temp)
            tail.next = new_node
            tail = tail.next
        return to_return_head