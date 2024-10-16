# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        prev = None
        curr = head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next


        return prev
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        if head is None:
            return True

        ## find midpoint of ll

        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        ## here since slow is midpoint we can break slow and reverse it 
        reversedList = self.reverseList(slow.next)

        first = head
        second = reversedList

        while first and second:
            if first.val != second.val:
                return False

            first = first.next
            second = second.next

        return True

