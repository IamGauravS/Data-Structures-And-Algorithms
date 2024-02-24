from Graph import Graph
# We only need Graph and Stack for this Challenge!

def get_children(llist):
    if llist.is_empty():
        return None

    output = []
    curr = llist.get_head()
    while curr != None:
        output.append(curr.data)
        curr = curr.next_element

    return output 

def dfs_cycle_check(g, source, visited, pathvisited):
    visited[source] = True 
    pathvisited[source] = True 

    children = get_children(g[source])
    if children != None:
      for c in children:
          if visited[c] == False:
              if (dfs_cycle_check(g, c, visited, pathvisited) == True):
                  return True 
          else:
              if pathvisited[c] == True:
                  return True 

    pathvisited[source] = False
    return False


def detect_cycle(g):
    # visited list to keep track of the nodes that have been visited
    # since the beginning of the algorithm
    visited = [False] * g.vertices
    # rec_node_stack keeps track of the nodes which are part of
    # the current recursive call
    pathvisited = [False] * g.vertices
    for node in range(g.vertices):
        # DFS recursion call
        if visited[node]:
            if dfs_cycle_check(g, node, visited, pathvisited):
                return True
    return False


