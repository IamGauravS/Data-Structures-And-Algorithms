from Graph import Graph
from Queue import MyQueue
from Stack import MyStack
# You can check the input directed graph in console tab

# Create Stack => stack = MyStack()
# Functions of Stack => push(int), pop(), top(), is_empty()
# Create Queue => queue = MyQueue()
# Functions of Queue => enqueue(int), dequeue(), size(), front(), is_empty()
# class Graph => {int vertices, linkedList[] array}
# class linkedList => {Node head_node}
# class Node => {int data, Node next_element}
# Depth First Traversal of Graph "g" from source vertex
def get_childred(llist):
    if llist.is_empty():
        return None 

    output = []
    curr = llist.get_head()
    while curr != None:
        output.append(curr.data)
        curr = curr.next_element

    return output


def dfs_traversal_helper(g, source, visited):
    output = ""
    stack = MyStack()
    stack.push(source)
    visited[source] = True
    while not stack.is_empty():
        value = stack.pop()
        output += str(value)
        children = get_childred(g.array[value])
        if children != None:
            for c in children:
                if visited[c] == False:
                    stack.push(c)
                    visited[c] = True
    
    return output, visited

def dfs_traversal(g, source):

    visited = [False]*g.vertices
    output = ""

    output, visited = dfs_traversal_helper(g, source, visited)

    for source in range(g.vertices):
        if visited[source] == False:
            temp, visited = dfs_traversal_helper(g, source, visited)
            output += temp 
    # Replace this placeholder return statement with your code
    return output
