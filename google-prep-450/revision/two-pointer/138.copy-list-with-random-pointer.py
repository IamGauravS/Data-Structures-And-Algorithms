#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToNewDict = {}

        curr = head
        oldToNewDict[None] = None 
        while curr:
            newNode = Node(curr.val)
            oldToNewDict[curr] = newNode 
            curr = curr.next

        curr = head 
        while curr:
            oldToNewDict[curr].next = oldToNewDict[curr.next]
            oldToNewDict[curr].random = oldToNewDict[curr.random]
            curr = curr.next

        return oldToNewDict[head]
    
# @lc code=end

