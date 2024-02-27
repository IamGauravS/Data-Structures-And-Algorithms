# NOTE: 'graph' has been created from the class 'Graph' in 'graph.py'

# class Graph => {int vertices, linkedList[] array}
# class LinkedList => {Node head_node}
# class Node => {int data, Node next_element}

def get_children(llist):
    if llist.is_empty():
        return None

    output = []
    curr = llist.get_head()
    while curr != None:
        output.append(curr.data)
        curr = curr.next_element

    return output 

def dfs(g, source, parent, visited):
    visited[source] = True
    children = get_children(g.array[source])
    if children != None:
        for c in children:
            if c != parent:
                if visited[c] == True:
                    return True 
                else:
                    if dfs(g, c, source, visited) == True:
                        return True 

    return False 

def detect_cycle_undirected_graph(g):
        cycle_flag = False   
        

        visited = [False]*g.vertices
        for v in range(g.vertices):
            if visited[v] == False:
                cycle_flag = dfs(g, v, -1, visited )
                if cycle_flag == True:
                    return True 

        return False 

def check_if_node_connected(g):
    visited = [False]*g.vertices
     
    stack_list = []
    stack_list.append(0)
    while  len(stack_list) != 0:
        curr = stack_list.pop()
        visited[curr] = True 
        children = get_children(g.array[curr])
        if children != None:
            for c in children:
                if visited[c] == False:
                    stack_list.append(c)

    if all(visited):
        return True
    else:
        return False 
    





def is_tree(g):
    
    if len(g.array) == 0:
        return True 
    check_cycle = detect_cycle_undirected_graph(g)
    if check_cycle == True:
        return False 
    check_connect = check_if_node_connected(g)
    if check_connect == False:
        return False 

    return True 
    # Replace this placeholder return statement with your code
    