from linked_list import LinkedList

# The code in "linked_list.py" can be used to create a linked list out of a list. 
# The code in "linked_list_traversal.py" can be used to traverse the linked list.
# The code in "linked_list_reversal.py" can be used to reverse the linked list.

def get_middle_node(head):

    # Replace this placeholder return statement with your code
    if head == None:
        return None 
    fast = head
    slow = head 
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next 

    return slow.data


