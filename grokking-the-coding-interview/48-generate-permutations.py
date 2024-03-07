def swap(s,i,j):
    s_list = list(s)
    s_list[i], s_list[j] = s_list[j], s_list[i]
    
    return "".join(s_list)


def permute_word_helper(word, i=0):
    if i == len(word) - 1:
        return [word]
    result = []
    for j in range(i, len(word)):
        swapped = swap(word, i, j)
        result += permute_word_helper(swapped, i + 1)
    return result

def permute_word(word):
    return permute_word_helper(word,0)