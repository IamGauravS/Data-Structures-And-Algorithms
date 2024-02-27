import queue

def generate_child(curr, array):
    child = []
    for num in array:
        temp = curr*num
        child.append(temp%(10**6))
    return child

def minimum_multiplication(start,end, array):

    dist = {}
    dist[start] = 0

    q = queue.Queue()
    q.put([0, start])

    while not q.empty():
        curr = q.get()
        step = curr[0]
        curr_num = curr[1]

        for child in generate_child(curr_num, array):
            if child < end:
                if child in dist:
                    if dist[child] > step+1:
                        dist[child] = step +1
                        q.put([step+1, child])
                else:
                    dist[child] = step+1
                    q.put([step+1, child])


    if end in dist:
        return dist[end]
    else:
        return -1