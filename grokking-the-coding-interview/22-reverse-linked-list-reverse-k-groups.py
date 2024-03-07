import math
from linked_list import LinkedList
from linked_list_node import LinkedListNode
from linked_list_traversal import traverse_linked_list
from linked_list_reversal import reverse_linked_list

def getKth(curr, k):
    while curr and k > 0:
        curr = curr.next
        k -= 1
    return curr

def reverse_k_groups(head, k):
    dummy = LinkedListNode(0)
    dummy.next = head
    groupPrev = dummy
    while True:
        kth = getKth(groupPrev, k)
        if not kth:
            break
        groupNext = kth.next

        prev, curr = kth.next, groupPrev.next
        while curr != groupNext:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        nextGroupPrev = groupPrev.next
        groupPrev.next = prev
        groupPrev = nextGroupPrev

    return dummy.next