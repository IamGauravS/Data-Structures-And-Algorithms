from trie import Trie

def find_strings(grid, words):
    trie = Trie()
    for word in words:
        trie.insert(word)

    result = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            dfs(grid, i, j, trie.root, '', result)
    return list(result)

def dfs(grid, i, j, node, word, result):
    if node.is_string:
        result.add(word)
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] not in node.children:
        return
    temp = grid[i][j]
    grid[i][j] = '' ### we do this so that we do not repeat this element
    dfs(grid, i + 1, j, node.children[temp], word + temp, result)
    dfs(grid, i - 1, j, node.children[temp], word + temp, result)
    dfs(grid, i, j + 1, node.children[temp], word + temp, result)
    dfs(grid, i, j - 1, node.children[temp], word + temp, result)
    grid[i][j] = temp