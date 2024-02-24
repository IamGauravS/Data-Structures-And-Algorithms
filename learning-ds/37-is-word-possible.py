from HashTable import HashTable

def is_formation_possible(lst, word):

    # Replace this placeholder return statement with your code
    word_set = set(lst)
    for w in word_set:
        start_index = word.find(w)
        if start_index == 0:
            secondword = word[start_index+len(w):]
            if secondword in word_set:
                return True 

    return False  