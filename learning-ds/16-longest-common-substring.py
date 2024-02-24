def build_suffix_array(text):
    n = len(text)
    suffixes = [(text[i:], i) for i in range(n)]
    suffixes.sort()

    suffix_array = [suffix[1] for suffix in suffixes]
    return suffix_array

def build_lcp_array(text, suffix_array):
    n = len(text)
    rank = [0] * n  # Initialize rank array

    # Assign ranks to all suffixes
    #the rank array is essentially the inverse of the suffix array. It tells you the rank (position in the sorted list of suffixes) of the suffix starting at each position in the string.
    for i in range(n):
        rank[suffix_array[i]] = i

    k = 0  # Initialize length of previous LCP
    lcp = [0] * n  # Placeholder to store LCP array

    # Process all suffixes one by one starting from first suffix in txt[]
    for i in range(n):
        # This condition is necessary to avoid index out of bounds
        if rank[i] == n - 1:
            k = 0
            continue

        # j contains index of the next substring to be considered to compare with the present substring, i.e., next string in suffix array
        j = suffix_array[rank[i] + 1]

        # Directly start matching from k'th index as at-least k-1 characters will match
        while i + k < n and j + k < n and text[i + k] == text[j + k]:
            k += 1  # k is the number of characters matched

        lcp[rank[i]] = k  # lcp for the present suffix.

        # Deleting the starting character from the string.
        if k > 0:
            k -= 1

    return lcp

def longest_common_substring(strings):
    if not strings or len(strings) < 2:
        return ""

    combined_text = "#".join(strings) + "#"
    suffix_array = build_suffix_array(combined_text)
    lcp_array = build_lcp_array(combined_text, suffix_array)

    max_length = 0
    max_index = 0

    for i in range(1, len(lcp_array)):
        if lcp_array[i] > max_length:
            # Check if the LCP is between suffixes from different strings
            if combined_text[suffix_array[i-1]:suffix_array[i-1]+lcp_array[i]].find("#") == -1 and combined_text[suffix_array[i]:suffix_array[i]+lcp_array[i]].find("#") == -1:
                max_length = lcp_array[i]
                max_index = i

    return combined_text[suffix_array[max_index]:suffix_array[max_index] + max_length]
# Example usage
if __name__ == '__main__':
    strings = ["banana", "apple", "experia"]
    
    common_substring = longest_common_substring(strings)

    print("Longest Common Substring:", common_substring)
