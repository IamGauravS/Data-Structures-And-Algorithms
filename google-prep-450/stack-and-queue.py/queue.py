class queueUsingStack:
    def __init__(self) -> None:
        self.size = 0
        self.stack = []

    def push(self, val):
        self.stack.append(val)
        self.size += 1


    def pop(self):
        if self.size == 0:
            return None 
        
        if len(self.stack) == 1:
            self.size -= 1
            return self.stack.pop()
        

        top = self.stack.pop()
        self.size -= 1

        item = self.pop()

        self.stack.append(top)
        self.size += 1

        return item 
    
    def front(self):
        if self.size == 0:
            return None 
        
        if len(self.stack) == 1:
            return self.stack[-1]
        
        top = self.stack.pop()
        self.size -= 1

        item = self.front()

        self.stack.append(top)
        self.size += 1

        return item 
    
    def getSize(self):
        return self.size 


class QueueUsingTwoStacks:
    def __init__(self) -> None:
        self.stack1 = []
        self.stack2 = []

    def push(self, val):
        self.stack1.append(val)

    def pop(self):
        if not self.stack1 and not self.stack2:
            return None

        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2.pop()

    def front(self):
        if not self.stack1 and not self.stack2:
            return None

        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2[-1]

    def getSize(self):
        return len(self.stack1) + len(self.stack2)