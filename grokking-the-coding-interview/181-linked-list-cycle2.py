from linked_list import LinkedList

def detect_cycle(head):
    if head == None or head.next == None:
        return None
    slow = head 
    fast = head 
    
    while fast and fast.next:
        slow = slow.next 
        fast = fast.next.next 
        if fast == slow:
            break
        
    if fast != slow:
        return None 

    curr = head
    while curr != slow:
        curr = curr.next
        slow = slow.next 
        
    return curr 