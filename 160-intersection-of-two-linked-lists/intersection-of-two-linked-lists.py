# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # data = set()
        tempA = headA
        tempB = headB
        
        # while tempA:
        #     data.add(tempA)
        #     tempA = tempA.next
        
        # while tempB:
        #     if tempB in data:
        #         return tempB
        #     tempB = tempB.next
        
        # return None

        lenA = 0
        lenB = 0
        while tempA:
            lenA += 1
            tempA = tempA.next
        while tempB:
            lenB += 1
            tempB = tempB.next
        
        if lenA > lenB:
            longer = headA
            shorter = headB
        else:
            longer = headB
            shorter = headA
        diff =  abs(lenA - lenB)
        while diff > 0:
            longer = longer.next
            diff -= 1
        
        # now both lists have equal length

        while longer:
            if longer == shorter: return longer
            longer = longer.next
            shorter = shorter.next
        
        return None
        