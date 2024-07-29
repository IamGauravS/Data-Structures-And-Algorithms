from collections import Counter

def longest_palindrome(words):
    # The built-in counter method is used to count the 
    # Frequencies of each word
    frequencies = Counter(words)
    count = 0
    central = False

    for word, frequency in frequencies.items():
        # If word is a palindrome
        if word[0] == word[1]:
            # If a word has even occurrences
            if frequency % 2 == 0:
                count += frequency
            # If a word has odd occurrences
            else:
                count += frequency - 1
                central = True

        # If word is not a palindrome
        # Ensuring that a word and its reverse is only considered once
        elif word[1] > word[0]:
            # Get the minimum of the occurrences of the word and its reverse
            count += 2 * min(frequency, frequencies[word[1] + word[0]])

    if central:
        count += 1

    return 2 * count

