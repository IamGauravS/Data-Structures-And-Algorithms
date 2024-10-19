class Solution:
    #Function to delete all the occurances of a key from the linked list.
    def deleteAllOccurOfX(self, head, x):
        dummyNode = Node(0)
        dummyNode.next = head
        
        if head:
            head.prev = dummyNode

        curr = dummyNode
    
        while curr.next:
            if curr.next.val == x:
                curr.next = curr.next.next
                if curr.next:
                    curr.next.prev = curr 

            else:
                curr = curr.next

        return dummyNode.next