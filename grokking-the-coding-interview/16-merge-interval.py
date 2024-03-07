def merge_intervals(intervals):

    # Replace this placeholder return statement with your code
    output = [intervals[0]]
    for i in range(1, len(intervals)):
        if output[-1][1] >= intervals[i][0]:
            curr = output.pop()
            if curr[1] < intervals[i][1]:
                curr[1] = intervals[i][1]
            output.append(curr)
        else:
            output.append(intervals[i])

    return output