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
        copyDict = {}
        copyDict[None] = None
        curr = head
        while curr:
            newNode = Node(curr.val)
            
            copyDict[curr] = newNode
            curr = curr.next

        
        curr = head

        while curr:
            newNode = copyDict[curr]
            newNode.next = copyDict[curr.next]
            newNode.random = copyDict[curr.random]
            curr = curr.next

        return copyDict[head]


## optimised version to use o(1) space

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # First pass: create new nodes and interleave them with original nodes
        curr = head
        while curr:
            newNode = Node(curr.val)
            newNode.next = curr.next
            curr.next = newNode
            curr = newNode.next

        # Second pass: assign random pointers for the new nodes
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        # Third pass: separate the original and copied nodes
        curr = head
        newHead = head.next
        while curr:
            copy = curr.next
            curr.next = copy.next
            if copy.next:
                copy.next = copy.next.next
            curr = curr.next

        return newHead

            