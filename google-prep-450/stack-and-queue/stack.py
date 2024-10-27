class Stack:
    def __init__(self):
        self.stack = []
        self.size = 0

    def push(self, val):
        self.stack.append(val)
        self.size += 1
        return 
    
    def pop(self):
        if self.size == 0:
            return None 
        
        val = self.stack.pop()
        self.size -= 1
        return val 
    
    def getSize(self):
        return self.size 
    
    def top(self):
        if self.size == 0:
            return None 
        return self.stack[-1]
    

import queue

class StackUsinghQueue:
    def __init__(self) -> None:
        self.queue1 = queue.Queue()
        self.queue2 = queue.Queue()
        self.size = 0 

    def push(self, val):
        self.queue2.put(val)
        self.size += 1

        while not self.queue1.empty():
            self.queue2.put(self.queue1.get())

        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self):
        if self.size == 0:
            return None 
        self.size -= 1
        return self.queue1.get()
    
    def top(self):
        return self.queue1.queue[0]
    
    def getSize(self):
        return self.size 
    

class stackUsingSingleQueue:
    def __init__(self) -> None:
        self.size = 0
        self.queue = queue.Queue()

    def push(self, val):
        self.queue.put(val)
        self.size += 1

        for _ in range(self.size - 1):
            self.queue.put(self.queue.get())

    def pop(self):
        if self.size == 0:
            return None 
        self.size -= 1
        return self.queue.get()
    
    def top(self):
        if self.size == 0:
            return None
        return self.queue.queue[0]
    
    def getSize(self):
        return self.size 