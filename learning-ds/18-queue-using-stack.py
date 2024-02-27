from Stack import MyStack
# Push Function => stack.push(int)  //Inserts the element at top
# Pop Function => stack.pop()       //Removes and returns the element at top
# Top/Peek Function => stack.get_top()  //Returns top element
# Helper Functions => stack.is_empty() & stack.isFull() //returns boolean

class NewQueue:
    def __init__(self):
        self.main_stack = MyStack()
        # Write your code here
        self.main_stack = MyStack()
        self.pop_stack = MyStack()


    # Inserts Element in the Queue
    def enqueue(self, value):
        # Write your code here
        self.main_stack.push(value)


    # Removes Element From Queue
    def dequeue(self):
        # Write your code here
        if not self.pop_stack.is_empty():
            return self.pop_stack.pop()
        else:
            while not self.main_stack.is_empty():
                self.pop_stack.push(self.main_stack.pop())
            return self.pop_stack.pop()