from Graph import Graph
from Queue import MyQueue
# You can check the input graph in console tab

# Create Queue => queue = MyQueue()
# Functions of Queue => enqueue(int), dequeue(), size(), front(), is_empty()
# Create Stack => stack = MyStack()
# Functions of Stack => push(int), pop(), top(), is_empty() 
# Create Graph => graph = Graph(vertices)
# Create LinkedList => link_list = LinkedList()
# Functions of LinkedList => insert_at_head(Node), is_empty(), delete(),
#                            delete_at_head(list), search(), print_list()
# class Node => data, next_element
# Breadth First Traversal of Graph g from source vertex
def get_children(llist):
    if llist.is_empty():
        return None 

    output = []
    curr = llist.get_head()
    while curr != None:
        output.append(curr.data)
        curr = curr.next_element

    return output

def bfs_traversal(g, source):

    # Replace this placeholder return statement with your code
    visited = [0]*g.vertices
    output = []
    queue = MyQueue()
    queue.enqueue(source)
    visited[source] = 1
    while not queue.is_empty():
        value = queue.dequeue()
        output.append(str(value))
        children = get_children(g.array[value])
        if children != None:
            for c in children:
                if visited[c] == 0:
                    queue.enqueue(c)
                    visited[c] = 1

    return "".join(output)
    