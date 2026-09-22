# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list1 is None:
            return list2
        if list2 is None:
            return list1

        init_flag = True
        while list1 or list2:
            temp_node = ListNode()
            if list1 and list2:
                if list1.val > list2.val:
                    temp_node.val = list2.val
                    list2 = list2.next
                else:
                    temp_node.val = list1.val
                    list1 = list1.next
            elif list2 is None:
                temp_node.val = list1.val
                list1 = list1.next
            elif list1 is None:
                temp_node.val = list2.val
                list2 = list2.next
            if init_flag:
                to_return_head = temp_node
                tail_node = to_return_head
                init_flag = False
            else:
                tail_node.next = temp_node
                tail_node = temp_node
        return to_return_head