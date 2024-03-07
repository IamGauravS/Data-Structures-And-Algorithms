def swap_pairs(head):

    dummy = LinkedListNode(0)
    dummy.next = head 
    prev = dummy 
    
    while head and head.next:
        first_node = head
        second_node = head.next

        # Swapping
        prev.next = second_node
        first_node.next = second_node.next
        second_node.next = first_node

        # Reinitializing the head and prev node
        prev = first_node
        head = first_node.next

    return dummy.next 
