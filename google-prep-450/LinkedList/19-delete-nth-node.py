# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        curr = head
        nthNodePointer = dummy
        
        # Move curr n steps ahead
        for _ in range(n):
            curr = curr.next
        
        # Move both pointers until curr reaches the end
        while curr:
            curr = curr.next
            nthNodePointer = nthNodePointer.next
        
        # Remove the nth node from the end
        nthNodePointer.next = nthNodePointer.next.next
        
        return dummy.next