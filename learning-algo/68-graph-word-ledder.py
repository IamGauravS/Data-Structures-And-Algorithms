import queue

def get_all_combs(curr_word, dictionary):
    # Initialize an empty list to store all combinations
    output_list = []
    # Get the ordinal value of 'a'
    ord_a = ord('a')
    # Convert the current word to a list of characters
    curr_word_list = list(curr_word)
    # Loop over each character in the current word
    for i in range(len(curr_word_list)):
        # Loop over each possible letter to replace the current character
        for j in range(26):
            # Copy the list of characters
            new_word_list = curr_word_list[:]
            # Replace the current character with a new letter
            new_word_list[i] = chr(ord_a+j)
            # Convert the list of characters back to a string
            new_word = ''.join(new_word_list)
            # If the new word is in the dictionary and is not the same as the current word
            if new_word in dictionary and new_word != curr_word:
                # Add the new word to the list of combinations
                output_list.append(new_word)

    # Return the list of all combinations
    return output_list

def find_word_ladder(source_word, dictionary, target_word):
    # Initialize a queue and add the source word to it
    q = queue.Queue()
    q.put(source_word)

    # Initialize dictionaries to keep track of the distance and path to each word
    # The distance to the source word is 0 and the path to the source word is just the source word itself
    distance = {source_word: 0}
    path = {source_word: [source_word]}

    # While there are still words in the queue
    while not q.empty():
        # Get the next word from the queue
        curr_word = q.get()
        # Get all possible combinations of the current word that are in the dictionary
        all_combs = get_all_combs(curr_word, dictionary)
        
        # Loop over each combination
        for comb in all_combs:
            # If we haven't visited this combination before
            if comb not in distance:
                # The distance to this combination is one more than the distance to the current word
                distance[comb] = distance[curr_word] + 1
                # The path to this combination is the path to the current word followed by the combination itself
                path[comb] = path[curr_word] + [comb]
                # Add the combination to the queue to explore its combinations in future iterations
                q.put(comb)
                # Remove the combination from the dictionary so we don't visit it again
                dictionary.remove(comb)

                # If the combination is the target word
                if comb == target_word:
                    # Return the distance to the target word and the path to the target word
                    return distance[comb], path[comb]