# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse_list(self, head):
        if head == None:
            return 
        prev = None 
        curr = head 
        while curr:
            next_node = curr.next
            curr.next = prev 
            prev = curr
            curr = next_node
            
        return prev
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 == None:
            return l2 
        if l2 == None:
            return l1 
        
        curr_l1 = l1 
        curr_l2 = l2
        carry = 0
        
        ## we will use l2 to store the answer
        while curr_l1 != None and curr_l2 != None:
            sum_num = curr_l1.val + curr_l2.val + carry
            curr_l2.val = sum_num % 10
            carry = sum_num // 10
            if curr_l1.next == None or curr_l2.next == None:
                break
            curr_l1 = curr_l1.next
            curr_l2 = curr_l2.next
            
            
        ## means we reached the end of l2 but not l1
        if curr_l1.next != None:
            curr_l1 = curr_l1.next
            while curr_l1:
                sum_num = curr_l1.val + carry 
                newNode = ListNode()
                newNode.val = sum_num % 10
                
                carry = sum_num // 10
                
                curr_l1 = curr_l1.next 
                curr_l2.next = newNode
                curr_l2 = newNode  
                
                
        if curr_l2.next != None:
            curr_l2 = curr_l2.next 
            while curr_l2 and carry:
                sum_num = curr_l2.val + carry 
                curr_l2.val = sum_num % 10
                carry = sum_num // 10
                if curr_l2.next == None:
                    break
                curr_l2 = curr_l2.next   
                
        if carry:
            newNode = ListNode(val= carry, next= None)
            curr_l2.next = newNode
            
        return l2
            
            
    
               
        
        
            
       
            
        
            
        
            
            