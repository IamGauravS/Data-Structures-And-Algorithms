# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None 

        tailNode = None
        curr = head
        totalNoOfNodes = 0

        while curr:
            if not curr.next:
                tailNode = curr
            totalNoOfNodes += 1
            curr = curr.next
            
        tailNode.next = head ## converted into circular list

        k = k % totalNoOfNodes

        headNodeIndex = totalNoOfNodes - k 
        curr = head

        headNodeIndex -= 1
        while headNodeIndex:
            curr = curr.next
            headNodeIndex -= 1

        head = curr.next
        curr.next = None 
        return head

        


