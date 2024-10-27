class MyQueue:

    def __init__(self):
        self.stack = []
        self.size = 0

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.size += 1

        return

    def pop(self) -> int:
        if self.size == 0:
            return None 

        if self.size == 1:
            item = self.stack.pop()
            self.size -= 1
            return item 

        top = self.stack.pop()
        self.size -= 1

        item = self.pop()

        self.stack.append(top)
        self.size += 1

        return item
        

    def peek(self) -> int:
        if self.size == 0:
            return None 

        if self.size == 1:
            item = self.stack[0]
            return item 

        top = self.stack.pop()
        self.size -= 1

        item = self.peek()

        self.stack.append(top)
        self.size += 1

        return item
        

    def empty(self) -> bool:
        if self.size == 0:
            return True
        return False 
        
