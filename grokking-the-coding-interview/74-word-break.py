def word_break(s, word_dict):
    word_set = set(word_dict)
    dp = [False] * (len(s) + 1)
    dp[0] = True

    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:  ##hecks if the substring s[0:j] can be segmented into dictionary words (i.e., dp[j] is True) and the substring s[j:i] is a dictionary word. If both conditions are True, it means the substring s[0:i] can be segmented into dictionary words.
                dp[i] = True
                break

    return dp[len(s)]