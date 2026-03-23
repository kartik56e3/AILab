def dls(graph, node, goal, depth_limit):
    if node == goal:
        return True
    
    if depth_limit <= 0:
        return False
    
    for neighbor in graph.get(node, []):
        if dls(graph, neighbor, goal, depth_limit - 1):
            return True
    
    return False


def iddfs(graph, start, goal, max_depth):
    for depth in range(max_depth + 1):
        print(f"Searching at depth: {depth}")
        if dls(graph, start, goal, depth):
            return True
    return False


# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

start_node = 'A'
goal_node = 'F'
max_depth = 3

found = iddfs(graph, start_node, goal_node, max_depth)

if found:
    print("Goal found!")
else:
    print("Goal not found within depth limit.")
