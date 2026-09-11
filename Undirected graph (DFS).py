def has_cycle_undirected(graph, n):
    visited = [False] * n
    
    def dfs(node, parent):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True
        return False
    
    for i in range(n):
        if not visited[i]:
            if dfs(i, -1):
                return True
    return False

# graph as adjacency list
graph = {0: [1], 1: [0, 2], 2: [1, 3], 3: [2, 1]}
print(has_cycle_undirected(graph, 4))  # True