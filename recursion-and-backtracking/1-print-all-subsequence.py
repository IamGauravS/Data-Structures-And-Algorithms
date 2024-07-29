def get_all_subsequence(input_str, output, index=0, subsequence=""):
    if index == len(input_str):
        output.append(subsequence)
        return
    get_all_subsequence(input_str, output, index + 1, subsequence + input_str[index])
    get_all_subsequence(input_str, output, index + 1, subsequence)

def print_all_subsequence(input_str):
    output = []
    get_all_subsequence(input_str, output)
    return output