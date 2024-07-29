from linked_list import *
from linked_list_node import *



def sort_list(head):
    if not head or not head.next:
        return head

    # Step 1: Divide the list into two halves
    prev, slow, fast = None, head, head
    while fast and fast.next:
        prev, slow, fast = slow, slow.next, fast.next.next
    prev.next = None

    # Step 2: Sort each half
    l1 = sort_list(head)
    l2 = sort_list(slow)

    # Step 3: Merge the sorted halves
    return merge(l1, l2)

def merge(l1, l2):
    dummy = LinkedListNode(0)
    curr = dummy

    while l1 and l2:
        if l1.data < l2.data:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next

    curr.next = l1 if l1 else l2

    return dummy.next