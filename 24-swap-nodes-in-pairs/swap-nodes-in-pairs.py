# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
       if not head or not head.next: return head

       dummy = ListNode()
       dummy.next = head
       prev = dummy
       curr = head

       while curr and curr.next:
           first_node = curr
           second_node = curr.next

           prev.next = second_node
           first_node.next = second_node.next
           second_node.next = first_node

           prev = first_node
           curr = first_node.next
        
       return dummy.next