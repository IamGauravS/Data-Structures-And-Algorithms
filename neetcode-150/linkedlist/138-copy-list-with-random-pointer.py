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
        if head == None:
            return None
        hashmap = {}
        
        
        curr = head
        
        while curr != None:
            newNode = Node(x = curr.val, next = None, random = None )
            hashmap[curr] = newNode            
            curr = curr.next
            
        curr = head
        while curr != None:
            newNode = hashmap[curr]
            if curr.next != None:
                newNode.next = hashmap[curr.next]
            if curr.random != None:
                newNode.random = hashmap[curr.random]
            curr = curr.next
            
        return hashmap[head]