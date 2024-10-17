# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: if the list is empty or has only one node
        if not head or not head.next:
            return head
        
        # Split the list into two halves using slow and fast pointers
        mid = self.getMid(head)  # Find the middle of the list
        left = head              # First half
        right = mid.next         # Second half
        mid.next = None          # Split the list
        
        # Recursively sort both halves
        left = self.sortList(left)
        right = self.sortList(right)
        
        # Merge the two sorted halves
        return self.mergeTwoLists(left, right)
    
    # Helper function to find the middle of the list
    def getMid(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    # Helper function to merge two sorted linked lists
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)  # Dummy node to simplify merging
        tail = dummy
        
        # Merge the two lists by comparing nodes
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        
        # Append any remaining nodes from either list
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        
        return dummy.next  # Return the merged sorted list starting from dummy's next
