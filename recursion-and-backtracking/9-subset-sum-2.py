## here we can have duplicates so we shouldnt have duplicate subset

def find_subset(index, nums, ds, output ):
    output.append(ds[:])
    for i in range(index, len(nums)):
        if i != index and nums[i] == nums[i-1]:  ## we do not pick duplicate if it is not the first index only in
            ## case of first index we do not look behind and pick it up
            continue 
        ds.append(nums[i])
        find_subset(i+1, nums, ds, output)
        ds.pop()


def subset_sum(arr):
    arr = sorted(arr)
    output = []
    find_subset(0, arr, [], output)
    return output 