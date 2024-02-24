def wildcard_match(str1, str2, i, j):
    # If str1 is empty, return True if str2 is also empty or contains only '*'
    if i<0:
        return all(x == '*' for x in str2[:j+1])
    # If str2 is empty but str1 is not, return False
    if j<0:
        return False 
    # If characters are same, move to the next characters
    if str1[i] == str2[j]:
        return wildcard_match(str1, str2, i-1, j-1)
    # If str1 has '*', it can be considered as an empty sequence or any character sequence
    if str1[i] == '*':
        count_once = wildcard_match(str1, str2, i-1, j-1)
        dont_count = wildcard_match(str1, str2, i, j-1)
        return count_once or dont_count
    # If str1 has '?', it can be considered as any single character
    if str1[i] == '?':
        return wildcard_match(str1, str2, i-1, j-1)
    # If characters are different and no wildcard characters are available, return False
    return False