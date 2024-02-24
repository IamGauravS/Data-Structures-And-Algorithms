import sys

def find_addition_chain(chain, n):
    if chain[len(chain) - 1] == n:
      return len(chain) -1
    
    min_len = sys.maxsize
  
    for i in range(len(chain)):
        for j in range(i, len(chain)):
            s = chain[i] + chain[j]
            if s<= n and s not in chain:
                chain.append(s)
                chain_len = find_addition_chain(chain, n)
                if chain_len < min_len:
                    min_len = chain_len
                
                chain.pop()


# ### The chain.pop() operation is used to backtrack. This is a common technique in recursive algorithms that explore multiple possibilities, such as this one.

# When the function adds a new sum s to the chain and makes a recursive call to explore the possibilities with this new chain, it's going down a specific path of the search tree. After it has fully explored this path (i.e., the recursive call returns), it needs to go back (or "backtrack") and explore other paths.

# The chain.pop() operation removes the last added sum s from the chain, effectively undoing the choice to add s to the chain. This allows the function to explore other possibilities in the next iterations of the loops.

# Without this backtracking step, the function would only explore one path of the search tree and would not necessarily find the shortest addition chain. By backtracking, the function ensures that it explores all possible addition chains and finds the shortest one.
#     return min_len + 1




n = 5
chain = [1]
chain_len = find_addition_chain(chain, n)
print(f"Minimum length addition chain for {n} is {chain_len}")
print(chain)