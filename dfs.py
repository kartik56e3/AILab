def dfs(graph, node, visited):
    visited.add(node)
    print(node, end=" ")

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


graph = {
    0: [1,2],
    1: [0,3,4],
    2: [0,5],
    3: [1],
    4: [1,5],
    5: [2,4]
}

visited = set()
dfs(graph, 0, visited)
