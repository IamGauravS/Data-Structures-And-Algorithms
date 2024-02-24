
prime = int(1e9 + 7)

# Recursive function to count distinct subsequences of s1 that match s2
def countUtil(s1, s2, ind1, ind2, dp):
    # If we have exhausted s2, we found a valid subsequence
    if ind2 < 0:
        return 1
    # If we have exhausted s1, but not s2, no valid subsequence found
    if ind1 < 0:
        return 0
    
    # If this subproblem has already been solved, return the cached result
    if dp[ind1][ind2] != -1:
        return dp[ind1][ind2]
    
    # If the current characters match, we can either choose to leave one character
    # or stay with the current character in s1
    if s1[ind1] == s2[ind2]:
        leaveOne = countUtil(s1, s2, ind1 - 1, ind2 - 1, dp)
        stay = countUtil(s1, s2, ind1 - 1, ind2, dp)
        
        # Store the result in the DP table and return it modulo prime
        dp[ind1][ind2] = (leaveOne + stay) % prime
        return dp[ind1][ind2]
    else:
        # If the characters don't match, we can only skip the character in s1
        dp[ind1][ind2] = countUtil(s1, s2, ind1 - 1, ind2, dp)
        return dp[ind1][ind2]
    
# Main function to count distinct subsequences of s1 that match s2
def subsequenceCounting(s1, s2, lt, ls):
    # Initialize a DP table to store intermediate results
    dp = [[-1 for j in range(ls)] for i in range(lt)]
    
    # Call the recursive function to count distinct subsequences
    return countUtil(s1, s2, lt - 1, ls - 1, dp)

def main():
    s1 = "abcabc"
    s2 = "abc"

    # Calculate and print the count of distinct subsequences
    print("The Count of Distinct Subsequences is", subsequenceCounting(s1, s2, len(s1), len(s2)))

if __name__ == "__main__":
    main()
