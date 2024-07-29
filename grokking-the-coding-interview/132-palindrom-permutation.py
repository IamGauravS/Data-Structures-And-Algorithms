from populating_hashmap import *


def permute_palindrome(st):

    # Replace this placeholder return statement with your code
    count_dict = {}
    
    for ch in st:
        if ch not in count_dict:
            count_dict[ch] = 0
        count_dict[ch] +=1 
        
    no_of_odds = 0
    for key, value in count_dict.items():
        if value % 2 == 1:
            no_of_odds +=1 
            
    return no_of_odds <= 1
