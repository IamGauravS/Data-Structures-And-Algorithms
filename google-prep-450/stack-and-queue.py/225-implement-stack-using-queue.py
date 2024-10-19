import queue
class MyStack:

    def __init__(self):
        self.size = 0
        self.queue = queue.Queue()

    def push(self, x: int) -> None:
        self.size += 1
        self.queue.put(x)

        # Move all previous elements behind the new one
        for _ in range(self.size - 1):
            self.queue.put(self.queue.get())

    def pop(self) -> int:
        if self.size == 0:
            return None 
        self.size -= 1  # Decrement the size after popping
        return self.queue.get()

    def top(self) -> int:
        if self.size == 0:
            return None
        
        return self.queue.queue[0]


    def empty(self) -> bool:
        return self.size == 0



