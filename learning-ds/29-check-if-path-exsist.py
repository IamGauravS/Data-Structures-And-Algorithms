from Graph import Graph
from Queue import MyQueue
# We only need Graph and Queue for this Question!

def find_child(llist):
    output = []
    curr = llist.get_head()
    if curr == None:
        return None 
    while curr != None:
        output.append(curr.data)
        curr = curr.next_element
    return output 

def dfs(g, source, visited):
    visited[source] = True 
    children = find_child(g.array[source])
    if children != None:
        for child in children:
            if visited[child] == False:
                visited = dfs(g, child, visited)

    return visited

def check_path(g, source, dest):

    # Replace this placeholder return statement with your code
    visited = [False] * g.vertices
    visited = dfs(g, source, visited)
    if visited[dest] == True:
        return True 
    else:
        return False 