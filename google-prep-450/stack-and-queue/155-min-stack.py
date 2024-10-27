class MinStack:

    def __init__(self):
        self.minStack = []
        self.stack = []
        self.size = 0
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.size == 0:
            self.minStack.append(val)
        else:
            if val < self.minStack[-1]:
                self.minStack.append(val)
            else:
                self.minStack.append(self.minStack[-1])

        self.size += 1
        return
        

    def pop(self) -> None:
        if self.size == 0:
            return None
        self.size -= 1
        self.minStack.pop()
        return self.stack.pop()

    def top(self) -> int:
        if self.size == 0:
            return None
        return self.stack[-1]

    def getMin(self) -> int:
        if self.size == 0:
            return None
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()