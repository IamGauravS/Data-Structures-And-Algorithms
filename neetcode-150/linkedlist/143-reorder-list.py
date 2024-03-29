class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # Find the middle of the list
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half of the list
        prev, curr = None, slow
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # Merge the two halves of the list
        first, second = head, prev
        while second.next:
            temp = first.next
            first.next = second
            first = temp

            temp = second.next
            second.next = first  ## here we have already updated first
            second = temp