# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list_1: Optional[ListNode], list_2: Optional[ListNode]) -> Optional[ListNode]:
        if not (list_1 and list_2): return (list_1 or list_2)
        head = ListNode()
        result = head

        while (list_1 and list_2):
            if list_1.val > list_2.val:
                head.next, list_2 = list_2, list_2.next
                head = head.next
            else:
                head.next, list_1 = list_1, list_1.next
                head = head.next
        if list_1:
            head.next = list_1

        if list_2:
            head.next = list_2
            
        return result.next
