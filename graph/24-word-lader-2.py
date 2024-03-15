
import sys
import queue

def get_children(curr_word, word_list):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    variations = set()
    for i in range(len(curr_word)):
        for letter in alphabet:
            variation = curr_word[:i] + letter + curr_word[i+1:]
            if variation != curr_word and variation in word_list:
                variations.add(variation)
                
    return variations

def word_lader_find_transformation(start_word, target_word, word_list):
    ## find the distance from start to target word only one letter can be changes and start word may or may not be the part of list
    
    distance = {}
    distance[start_word] = 0
    
    for word in word_list:
        distance[word] = sys.maxsize
        
    distance[start_word] = 0
    q = queue.Queue()
    
    q.put((start_word, 0))
    parent = {}
    
    for key in distance:
        parent[key] = None 
        
    
    parent[start_word] = None
    
    while q:
        curr_word, curr_distance = q.get()
        
        children = get_children(curr_word, word_list)
        for c in children:
            if distance[c] > 1 + curr_distance:
                distance[c] = 1 + curr_distance
                q.put((c, distance[c]))
                parent[c] = curr_word
                
                
    curr =  target_word
    output = []
    
    while curr != None:
        output.append(curr)
        curr = parent[curr]
                
    return output[::-1]
    