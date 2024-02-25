import queue

def course_schedule(task_list):
    adj_list = {}
    for task in task_list:
        if task[1] in adj_list:
            adj_list[task[1]].append(task[0])
        else:
            adj_list[task[1]] = [task[0]]

    # Use a dictionary for indegree to handle arbitrary task numbers/labels
    indegree = {node: 0 for node in adj_list.keys()}

    for node in adj_list.keys():
        for child in adj_list[node]:
            indegree[child] += 1

    q = queue.Queue()
    for node in indegree.keys():
        if indegree[node] == 0:
            q.put(node)

    topo = []
    while not q.empty():
        curr = q.get()
        topo.append(curr)
        for child in adj_list[curr]:
            indegree[child] -= 1
            if indegree[child] == 0:
                q.put(child)

    # Return True if all tasks are included in the topological sort (i.e., no cycle in the graph)
    return len(topo) == len(adj_list)