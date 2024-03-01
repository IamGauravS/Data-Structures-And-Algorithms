from linked_list import LinkedList
from linked_list_node import LinkedListNode
            
def reverse(head):

    # Replace this placeholder return statement with your code
    prev = None 
    curr = head 
    

    while curr != None:
        next = curr.next 
        curr.next = prev 
        prev = curr 
        curr = next 

    return prev 
