
def letter_combination_helper(digits, i, output_list, phone_dict, curr):
    if i == len(digits):
        temp = "".join(curr)
        output_list.append(temp)
    else:
        for j in range(len(phone_dict[int(digits[i])])):
            curr.append(phone_dict[int(digits[i])][j])
            letter_combination_helper(digits, i+1, output_list, phone_dict, curr)
            curr.pop()
            
    return output_list
            
    

def letter_combinations(digits):
    # Replace this placeholder return statement with your code
    if not digits:
        return []
    output_list = []
    phone_dict = {}
    phone_dict[1] = []
    phone_dict[2] = ["a", "b", "c"]
    phone_dict[3] = ["d", "e", "f"]
    phone_dict[4] = ["g", "h", "i"]
    phone_dict[5] = ["j", "k", "l"]
    phone_dict[6] = ["m", "n", "o"]
    phone_dict[7] = ["p", "q", "r", "s"]
    phone_dict[8] = ["t", "u", "v"]
    phone_dict[9] = ["w", "x", "y", "z"]
    
    output_list = letter_combination_helper(digits, 0, output_list, phone_dict, [])
    return output_list