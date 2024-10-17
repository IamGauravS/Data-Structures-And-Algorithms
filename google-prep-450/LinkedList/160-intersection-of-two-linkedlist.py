# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        
        # Two pointers starting at the heads of A and B
        pointerA = headA
        pointerB = headB
        
        # Traverse both lists. When one pointer reaches the end, switch to the other list's head
        while pointerA != pointerB:
            pointerA = pointerA.next if pointerA else headB
            pointerB = pointerB.next if pointerB else headA
        
        # Either they meet at the intersection, or both are None (no intersection)
        return pointerA
