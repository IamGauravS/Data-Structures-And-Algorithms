from Queue import MyQueue
from Stack import MyStack

def reverseK(queue, k):
    
    if k > queue.size() or k < 0:
        return None

    temp_stack = MyStack()
    for i in range(k):
        temp_stack.push(queue.dequeue())
    queue_new = MyQueue()
    while not temp_stack.is_empty():
        queue_new.enqueue(temp_stack.pop())
    while not queue.is_empty():
        queue_new.enqueue(queue.dequeue())
    return queue_new

# optimal solution
# 1.Push first k elements in queue in a stack.
# 2.Pop Stack elements and enqueue them at the end of queue
# 3.Dequeue queue elements till "k" and append them at the end of queue