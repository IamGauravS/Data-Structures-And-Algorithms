def k_smallest_pairs(list1, list2, k):
    list_length = len(list1)
    min_heap = []
    pairs = []

    for i in range(min(k, list_length)):
        heappush(min_heap, (list1[i] + list2[0], i, 0))

    counter = 1

    while min_heap and counter <= k:
        sum_of_pairs, i, j = heappop(min_heap)
        pairs.append([list1[i], list2[j]])

        next_element = j + 1  ## we dont run a loop we just take the next element from popped value

        if len(list2) > next_element:
            heappush(min_heap,
                     (list1[i] + list2[next_element], i, next_element))

        counter += 1

    return pairs