from Graph import Graph
from Queue import MyQueue

def get_children(llist):
    if llist.is_empty():
        return None

    output = []
    curr = llist.get_head()
    while curr != None:
        output.append(curr.data)
        curr = curr.next_element

    return output 

def find_min(g, a, b):

    # Replace this placeholder return statement with your code
    distance = [-1]*g.vertices
    visited = [False]*g.vertices
    queue = MyQueue()
    queue.enqueue(a)
    visited[a] = True 
    distance[a] = 0
    while not queue.is_empty():
        curr = queue.dequeue()
        children = get_children(g.array[curr])
        if children != None:
            for c in children:
                if visited[c] == False:
                    queue.enqueue(c)
                    visited[c] = True
                    distance[c] = distance[curr] + 1

                if c == b:
                    return distance[c]

    return -1
        