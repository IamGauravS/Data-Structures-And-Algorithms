from collections import defaultdict, deque

def alien_order(words):
    graph = defaultdict(set)
    in_degree = {c: 0 for word in words for c in word}

    # Construct the graph
    for i in range(1, len(words)):
        word1, word2 = words[i - 1], words[i]
        for j in range(min(len(word1), len(word2))):
            if word1[j] != word2[j]:
                if word2[j] not in graph[word1[j]]:
                    graph[word1[j]].add(word2[j])
                    in_degree[word2[j]] += 1
                break

    # Perform topological sort
    queue = deque([c for c in in_degree if in_degree[c] == 0])
    result = ''
    while queue:
        curr = queue.popleft()
        result += curr
        for neighbor in graph[curr]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Check for cycle
    if len(result) != len(in_degree):
        return ''
    return result

# Example usage:
