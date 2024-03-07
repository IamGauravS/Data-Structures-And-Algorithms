from collections import deque


def find_max_sliding_window(nums, w):

    # Replace this placeholder return statement with your code
    dq = deque()
    for i in range(w):
        dq.append(nums[i])

    max_array = []
    max_array.append(max(dq))
    for i in range(w, len(nums)):
        dq.popleft()
        dq.append(nums[i])
        max_array.append(max(dq))


    return max_array