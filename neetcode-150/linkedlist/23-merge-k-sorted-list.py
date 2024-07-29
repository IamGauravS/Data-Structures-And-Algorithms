# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeSortedList(self, l1, l2):
        if l1 is None:
            return l2 
        if l2 is None:
            return l1 
        
        dummy = ListNode()
        curr = dummy
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1 
                l1 = l1.next
            else:
                curr.next = l2 
                l2 = l2.next 
            curr = curr.next 
            
        if l1:
            curr.next = l1 
        if l2:
            curr.next = l2
             
        return dummy.next
            
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        
        for i in range(1, len(lists)):
            lists[0] = self.mergeSortedList(lists[0], lists[i])
            
        return lists[0]
    
    
    
    
### if we are allowed to use extra space


import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        heap = []

        for i in range(len(lists)):
            if lists[i] is not None:
                heapq.heappush(heap, (lists[i].val, i))
                lists[i] = lists[i].next

        while heap:
            val, i = heapq.heappop(heap)
            curr.next = ListNode(val)
            curr = curr.next

            if lists[i] is not None:
                heapq.heappush(heap, (lists[i].val, i))
                lists[i] = lists[i].next

        return dummy.next
    
    
    
## two at  atime

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None 
        ## merge 2 at a time
        while len(lists) > 1:
            mergedLists = []
            
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1) < len(lists) else None
                mergedLists.append(self.mergeList(l1, l2))
                
            lists = mergedLists
            
        return lists[0]