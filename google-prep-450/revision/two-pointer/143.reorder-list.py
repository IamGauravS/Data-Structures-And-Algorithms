#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        fast, slow = head , head
        

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        ##list has either one or two element
        if fast == slow:
            return 
        
        ll2 = slow.next 
        slow.next = None 

        def reverse(head):
            curr = head 
            prev = None 

            while curr:
                next = curr.next 
                curr.next = prev
                prev = curr 
                curr = next 

            return prev 

        ll2 = reverse(ll2)

        head1, head2 = head, ll2 

        while head1 and head2:
            next1 = head1.next 
            next2 = head2.next 

            head1.next = head2 
            head2.next = next1 

            head1 = next1 
            head2 = next2 

        return  


# @lc code=end

