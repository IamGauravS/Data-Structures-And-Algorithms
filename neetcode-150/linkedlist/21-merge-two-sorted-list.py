# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2 
        if list2 == None:
            return list1 
        
        curr1 = list1
        curr2 = list2 
        tempNode = ListNode()
        tempNode.next = list1 
        curr1 = tempNode
        while curr1 != None:
            if curr2 != None and curr1.next != None and  curr1.next.val > curr2.val:
                next_node = curr1.next 
                curr1.next = curr2 
                curr2 = curr2.next
                curr1.next.next = next_node
                
            
            
            if curr1.next == None and curr2 != None:
                curr1.next  = curr2 
                break
                
            curr1 = curr1.next
                
        return tempNode.next
                
                
## simplified

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2 
        if list2 is None:
            return list1 

        dummy = ListNode(0)
        curr = dummy

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        # At this point, we reached the end of one of the lists
        # The remaining list should be linked to the end of the merged list
        if list1 is not None:
            curr.next = list1
        else:
            curr.next = list2

        return dummy.next