class Node:
    def __init__ (self,value):
        self.value = value 
        self.next = None

class LinkedList:
    def __init__(self, head = None):
        self.head = head 

    def append(self, new_node):
        current = self.head 
        if current == None:
            self.head = new_node
        else:
            while current.next:
                current = current.next 
                
            current.next = new_node

    def delete(self, value):
        curr = self.head 
        if curr.value == value:
            self.head = curr.next 

        else:
            while curr:
                if curr.value == value:
                    break 
                prev = curr 
                curr = curr.next 
            if curr ==None:
                return 
            
            prev.next = curr.next 
            curr = None 

    def insert(self, new_element, position):
        curr = self.head 
        count = 1
        if position == 1:
            new_element.next = self.head 
            self.head = new_element
        else:
            while curr: 
                if count + 1 == position:
                    temp = curr.next
                    curr.next = new_element
                    new_element.next = temp 
                    return
                elif curr.next == None:
                    curr.next = new_element
                    return  
                else:
                    curr = curr.next 
                    count+=1


    def print(self):
        curr = self.head 
        while curr:
            print(curr.value)
            curr = curr.next