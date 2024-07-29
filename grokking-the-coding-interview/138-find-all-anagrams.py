def find_anagrams(a, b):
    if len(a) < len(b):
      return []
    freq_count_b = {}
    for ch in b:
        if ch not in freq_count_b:
            freq_count_b[ch] = 0
        freq_count_b[ch] += 1

    freq_count_a = {}
    output_list = []

    # Initialize the frequency count for the first window in a
    for k in range(len(b)):
        if a[k] not in freq_count_a:
            freq_count_a[a[k]] = 0
        freq_count_a[a[k]] += 1

    # Check if the first window is an anagram
    if freq_count_a == freq_count_b:
        output_list.append(0)

    # Sliding window approach to find anagrams
    for j in range(len(b), len(a)):
        # Remove the leftmost character from the current window
        freq_count_a[a[j - len(b)]] -= 1

        # Add the rightmost character to the current window
        if a[j] not in freq_count_a:
            freq_count_a[a[j]] = 0
        freq_count_a[a[j]] += 1

        # Check if the current window is an anagram
        if freq_count_a == freq_count_b:
            output_list.append(j - len(b) + 1)

    return output_list
