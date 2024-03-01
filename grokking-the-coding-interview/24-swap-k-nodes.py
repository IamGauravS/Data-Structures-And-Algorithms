def swap_nodes(head, k):

    
    curr = head 
    prev = None 
    while k>0:
        prev = curr 
        curr = curr.next 
        k -= 1 

    firstnode = prev 

    second = head 
    while curr != None:
        curr = curr.next
        second = second.next 

    swap (firstnode, second)
    
    return head