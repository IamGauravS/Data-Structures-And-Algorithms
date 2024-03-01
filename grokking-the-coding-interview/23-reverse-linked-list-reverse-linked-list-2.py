from linked_list import LinkedList
from linked_list_node import LinkedListNode
from linked_list_traversal import traverse_linked_list
from linked_list_reversal import reverse_linked_list
            
def reverse_between(head, left, right):

  # Replace this placeholder return statement with your code
  prevgroup = None 
  curr = head 
  k = 1
  while k < left and curr != None:
    prevgroup = curr 
    curr = curr.next 
    k +=1

  prev = None 
  curr_groupstart = curr 
  k = 0
  while k <= (right-left):
    next = curr.next 
    curr.next = prev 
    prev = curr 
    curr = next
    k+=1 

  if prevgroup != None:
    curr_groustart  = prevgroup.next
    prevgroup.next = prev 
    curr_groupstart.next = curr 

  else:
    head = prev 


  




  return head
