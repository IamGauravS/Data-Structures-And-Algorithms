from union_find import UnionFind

from union_find import *

def longest_consecutive_sequence(nums):
    if len(nums) == 0:
        return 0
    # data structure for implementing union find
    ds = UnionFind(nums)

    for num in nums:
        # check if the next consecutive number 
        # is in the input array
        if num + 1 in ds.parent:
            ds.union(num, num + 1)

    return ds.max_length