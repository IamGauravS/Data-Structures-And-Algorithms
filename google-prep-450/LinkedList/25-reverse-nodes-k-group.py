# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getKthNode(self, temp, k):
        k -= 1
        while k > 0 and temp != None:
            k -= 1
            temp = temp.next 

        return temp 
    
    def reverseLinkedList(self, temp):
        prev = None 
        curr = temp 

        while curr:
            next = curr.next 
            curr.next = prev 
            prev = curr 
            curr = next 

        return prev

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        temp = head 
        prevLast = None 

        while temp != None:
            kthNode = self.getKthNode(temp, k)
            if kthNode == None:
                if prevLast:
                    prevLast.next = temp 
                    break 

            nextNode = kthNode.next 
            kthNode.next = None 
            self.reverseLinkedList(temp)

            if temp == head:
                head = kthNode
            else:
                prevLast.next = kthNode

            prevLast = kthNode
            temp = nextNode


        return head
                
            