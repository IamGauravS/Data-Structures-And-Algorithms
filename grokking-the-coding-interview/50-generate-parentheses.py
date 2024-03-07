def generate_paranthesis_helper(curr_str, opening_count, closing_count, n, result):
    if opening_count == closing_count == n:
        result.append(curr_str)
    if opening_count < n:
        generate_paranthesis_helper(curr_str + "(", opening_count+1, closing_count, n, result)
    if closing_count < opening_count:
        generate_paranthesis_helper(curr_str + ")", opening_count, closing_count+1, n, result)
    return result

def generate_combinations(n):
    result = []
    result = generate_paranthesis_helper("", 0, 0, n, result)
    return result