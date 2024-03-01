from collections import Counter, OrderedDict
def task_schedulars(task, n):

    counter = Counter(task)
    sorted_list = OrderedDict(sorted(counter.items(), key=lambda item: item[1], reverse=True))

    max_freq = sorted_list.popitem()[1]
    idle_time = (max_freq-1) * n
    while sorted_list and idle_time >0:
        idle_time = idle_time - min(max_freq-1, sorted_list.popitem()[1])

    idle_time = max(idle_time, 0)
    return len(task) + idle_time

#https://www.educative.io/courses/grokking-coding-interview-patterns-python/solution-task-scheduler