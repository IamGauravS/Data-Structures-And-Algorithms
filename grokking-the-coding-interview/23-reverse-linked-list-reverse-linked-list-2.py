def reorder_list(head):
    if not head:
        return

    # Find the middle of the list
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse the second half
    prev, curr = None, slow
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    # Merge the first and second half
    first, second = head, prev
    while second.next:
        first.next, first = second, first.next
        second.next, second = first, second.next

    return head