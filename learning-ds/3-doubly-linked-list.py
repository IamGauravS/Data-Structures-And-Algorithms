class Node:
    def __init__(self, value):
        self.value = value 
        self.prev = None 
        self.next = None 


    def __repr__(self):
        return str(self.value)

class DoublyLinkedList(object):

    def __init__(self):
         self.llsize = 0
         self.head = None 
         self.tail = None 
         self.travIter = None 

    def __len__(self):
        return self.llsize
    
    def clear(self):
        curr = self.head
        while curr:
            next = curr.next 
            curr.next, curr.prev = None 
            curr.value = None 
            curr = next 

        self.llsize = 0
        self.head = 0
        self.tail = 0
        curr = None 

    def selze(self):
        return self.llsize
    
    def isEmpty(self):
        if self.llsize == 0:
            return True 
        else:
            return False 
        
    def add(self, elem):
        self.addLast(elem)

    def addLast(self, elem):
        if self.isEmpty():
            self.head = self.tail = Node(elem, None, None)
        else:
            self.tail.next = Node(elem, self.tail, None)
            self.tail = self.tail.next 

        self.llsize +=1 

    def addFirst(self, elem):
        if self.isEmpty():
            self.head = self.tail = Node(elem, None, None)
        else:
            self.head.prev = Node(elem, None, self.head)
            self.head = self.head.prev 

        self.llsize +=1 

    def addAt(self, index, data):
        ## add an element to a particular index
        if index < 0:
            raise Exception("index should be positive")
        
        if index == 0:
            self.addFirst(data)
            return

        if index == self.llsize:
            self.addLast(data)
            return 
        
        temp = self.head 
        for i in range(index-1):
            temp = temp.next 

        newNode = Node(data, temp, temp.next)
        temp.next.prev = newNode
        temp.next = newNode

        self.llsize += 1

    def peekFirst(self):
        if self.isEmpty():
            raise Exception("list is empty")
        return self.head.value
    
    def peekLast(self):
        if self.isEmpty():
            raise Exception("list is empty")
        return self.tail.value 
    
    def removeFirst(self):

        if self.isEmpty():
            raise Exception("list is empty")
        
        data = self.head.value
        self.head = self.head.next
        self.llsize -=1

        if self.isEmpty():
            self.tail = None 

        else:
            self.head.prev = None 

        return data
    
    def removeLast(self):

        if self.isEmpty():
            raise Exception("list is empty")
        
        data = self.tail.value 
        self.tail = self.tail.prev
        self.llsize -=1

        if self.isEmpty():
            self.head = None 

        else:
            self.tail.next = None 

        return data 
    
    def __remove__(self, node):

        if node.prev == None: ## head node
            return self.removeFirst()
        
        if node.next == None: ## tail node
            return self.removeLast()
        
        node.next.prev = node.prev 
        node.prev.next = node.next 

        data = node.data 

        node.data = None
        node.prev, node.next = None 
        node = None 

        self.llsize -= 1
        return data 
    
    def removeAt(self, index):

        if index <0 or index >= self.llsize:
            raise Exception("index out of bounds")
        
        if index < self.llsize /2:
            i = 0
            trev = self.head
            while i != index:
                i+=1
                trav = trav.next 

        else:
            i = self.llsize-1
            trav = self.tail
            while i != index:
                i -=1
                trav = trav.prev 

        return self.__remove__(trav)
    
    

        
    
    

