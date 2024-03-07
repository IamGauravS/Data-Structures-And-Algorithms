from linked_list import LinkedList
from linked_list_reverse import reverse_linked_list


def palindrome(head):

    # Replace this placeholder return statement with your code
    slow = head 
    fast = head 
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next 

    ## reverse 
    reversed_half = reverse_linked_list(slow)
    first = head 
    reverse = reversed_half

    while reverse != None and first != None:
        if reverse.data != first.data:
            return False 
        reverse = reverse.next 
        first = first.next 

    return True
