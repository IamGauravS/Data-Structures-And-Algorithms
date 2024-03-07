from linked_list import LinkedList

def detect_cycle(head):
   if head is None:
      return False 
   # Replace this placeholder return statement with your code
   slow = head 
   if slow.next == None:
      return False

   fast = head.next.next 
   
   while fast != None:
      if fast == slow:
         return True 
      slow = slow.next 
      if fast.next == None:
         return False 
      fast = fast.next.next 
      


   return False