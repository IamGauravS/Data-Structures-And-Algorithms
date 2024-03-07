def find_repeated_sequences(s, k):

    # Replace this placeholder return statement with your code
    first = 0
    last = k
    data_dict = {}
    output_set = set()
    while last <= len(s):
        if s[first:last] in data_dict:
            output_set.add(s[first:last])
        else:
            data_dict[s[first:last]] = 1
        first +=1
        last +=1


    return output_set