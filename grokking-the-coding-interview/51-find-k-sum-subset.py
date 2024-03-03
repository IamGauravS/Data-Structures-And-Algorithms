def get_k_sum_subsets_helper(set_of_integers, target_sum, i, curr_sum, output, curr_list):
    if i == len(set_of_integers):
        if curr_sum == target_sum:
            output.append(curr_list.copy())
        return

    # Include the current element in the subset
    curr_list.append(set_of_integers[i])
    get_k_sum_subsets_helper(set_of_integers, target_sum, i+1, curr_sum + set_of_integers[i], output, curr_list)
    curr_list.pop()

    # Exclude the current element from the subset
    get_k_sum_subsets_helper(set_of_integers, target_sum, i+1, curr_sum, output, curr_list)

def get_k_sum_subsets(set_of_integers, target_sum):
    output = []
    get_k_sum_subsets_helper(set_of_integers, target_sum, 0, 0, output, [])
    return output





def get_k_sum_subsets_helper(set_of_integers, target_sum, i, curr_sum, output, curr_list):
    if curr_sum == target_sum:
        output.append(curr_list.copy())
        return
    if i == len(set_of_integers) or curr_sum > target_sum:
        return

    # Include the current element in the subset
    curr_list.append(set_of_integers[i])
    get_k_sum_subsets_helper(set_of_integers, target_sum, i+1, curr_sum + set_of_integers[i], output, curr_list)
    curr_list.pop()

    # Exclude the current element from the subset
    get_k_sum_subsets_helper(set_of_integers, target_sum, i+1, curr_sum, output, curr_list)

def get_k_sum_subsets(set_of_integers, target_sum):
    output = []
    get_k_sum_subsets_helper(set_of_integers, target_sum, 0, 0, output, [])
    return output