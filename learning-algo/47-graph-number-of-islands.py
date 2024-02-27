### input unidrected graph [{1: [1,0,1], 2: [2,1,1], 3: [1,3,1]}


def dfs(graph, starting_node, visiting_list):
    stack = []
    stack.append(starting_node)

    while len(stack) != 0:
        curr = stack.pop()
        visiting_list[curr] = True 
        children = graph[curr]
        for child in children:
            if not visiting_list[child]:
                stack.append(child)


def find_provinces(graph):
    visited_array = [False]*len(max(graph.keys()) + 1)
    island_count = 0
    for key in graph.keys():
        if visited_array[key] == False:
            island_count +=1
            dfs(graph, key, visited_array)

    return island_count