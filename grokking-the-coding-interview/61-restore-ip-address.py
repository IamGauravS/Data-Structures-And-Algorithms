def valid(segment):
    segment_length = len(segment)
    if segment_length > 3:
        return False

    return int(segment) <= 255 if segment[0] != '0' else len(segment) == 1


# this function will append the current list of segments to the list of results.
def update_segment(s, curr_dot, segments, result):
    segment = s[curr_dot + 1:len(s)]

    if valid(segment): 
        segments.append(segment)
        result.append('.'.join(segments))
        segments.pop() 


def backtrack(s, prev_dot, dots, segments, result):

    size = len(s)

    for curr_dot in range(prev_dot + 1, min(size - 1, prev_dot + 4)):
        segment = s[prev_dot + 1:curr_dot + 1]
        if valid(segment):
            segments.append(segment)

            if dots - 1 == 0:
                update_segment(s, curr_dot, segments, result)
            else:
                backtrack(s, curr_dot, dots - 1, segments, result)

            segments.pop()


def restore_ip_addresses(s):

    result, segments = [], []
    backtrack(s, -1, 3, segments, result)
    return result


# driver code
