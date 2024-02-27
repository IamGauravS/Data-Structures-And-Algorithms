from Graph import Graph
from Queue import MyQueue
from Stack import MyStack
# You can check the input graph in console tab

# Create Stack => stack = MyStack()
# Functions of Stack => push(int), pop(), top(), is_empty()
# Create Queue => queue = MyQueue()
# Functions of Queue => enqueue(int), dequeue(), size(), front(), is_empty()
# class Graph => {int vertices, linkedList[] array}
# class linkedList => {Node head_node}
# class Node => {int data, Node next_element}
def check_list(visited):
    if all(visited):
        return True 
    return False


def find_children(llist):
    output = []
    if llist.is_empty():
        return None 
    else:
        current = llist.get_head()
        while current != None:
            output.append(current.data)
            current = current.next_element

        return output


def find_mother_vertex_rec(g, source, visited):
    visited[source] = True
    if check_list(visited):
        return True 

    children = find_children(g.array[source])
    if children != None:
        for c in children:
            if visited[c] == False:
                find_mother_vertex_rec(g, c, visited)
                    
    
    return check_list(visited)
    


def find_mother_vertex(g):

    # Replace this placeholder return statement with your code
    flag = False 
    for v in range(g.vertices):
        visited = [False]*g.vertices
        flag = find_mother_vertex_rec(g, v, visited)
        if flag == True:
            return v 

    return -1

# Create helper functions here