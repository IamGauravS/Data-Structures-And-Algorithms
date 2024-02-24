def build_suffix_array(text):
    n = len(text)
    suffixes = [(text[i:], i) for i in range(n)]
    suffixes.sort()

    suffix_array = [suffix[1] for suffix in suffixes]
    return suffix_array

# Example usage
if __name__ == '__main__':
    text = "banana"
    suffix_array = build_suffix_array(text)

    print("Suffix Array for '{}' is:".format(text))
    print(suffix_array)

