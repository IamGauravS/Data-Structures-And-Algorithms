
def find_one_char_diff_words(word, word_set):
    one_char_diff_words = []
    for w in word_set:
        if len(w) != len(word):
            continue
        diff_count = sum(1 for wc, ww in zip(w, word) if wc != ww)
        if diff_count == 1:
            one_char_diff_words.append(w)
    return one_char_diff_words

from collections import deque
def word_ladder(src, dest, words):
    # Replace this placeholder return statement with your code
    word_set = set(words)
    distance = 0
    visited = {}
    
    for word in word_set:
        visited[word] = False
    q = deque()
    q.append(src)
    visited[src] = True
    
    while q:
        
        q_len = len(q)
        distance +=1
        
        for _ in range(q_len):
            
            
            curr_word = q.popleft()
            
            if curr_word == dest:
                return distance
            
            
            visited[curr_word] = True 
            
            children = find_one_char_diff_words(curr_word, word_set)
            for c in children:
                if not visited[c]:
                    q.append(c)
                    visited[c] = True
                    
                    
    return 0
                
