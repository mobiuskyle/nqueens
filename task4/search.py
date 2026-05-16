# CCS 2226 - Foundation of AI
# Task 4 - BFS and DFS Search
# Author: mobiuskyle

from collections import deque

# GRAPH (map of connected nodes)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E', 'G'],
    'G': ['F']
}

# BREADTH FIRST SEARCH (BFS)
# Explores level by level (uses a queue)

def bfs(graph, start, goal):
    print("\n--- BREADTH FIRST SEARCH (BFS) ---")
    print(f"Start: {start} | Goal: {goal}\n")

    visited = []          # Tracks visited nodes
    queue = deque()       # Queue for BFS

    queue.append([start]) # Start with initial node

    while queue:
        path = queue.popleft()   # Take the first path
        node = path[-1]          # Get last node in path

        if node not in visited:
            visited.append(node)
            print(f"Visiting: {node} | Path so far: {' -> '.join(path)}")

            if node == goal:
                print(f" Goal '{goal}' found!")
                print(f"Final Path: {' -> '.join(path)}")
                return path

            # Add neighbors to queue
            for neighbor in graph[node]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    print(" Goal not found.")
    return None


# DEPTH FIRST SEARCH (DFS)
# Explores as deep as possible (uses a stack)

def dfs(graph, start, goal):
    print("\n--- DEPTH FIRST SEARCH (DFS) ---")
    print(f"Start: {start} | Goal: {goal}\n")

    visited = []          # Tracks visited nodes
    stack = [[start]]     # Stack for DFS

    while stack:
        path = stack.pop()       # Take the last path
        node = path[-1]          # Get last node in path

        if node not in visited:
            visited.append(node)
            print(f"Visiting: {node} | Path so far: {' -> '.join(path)}")

            if node == goal:
                print(f"Goal '{goal}' found!")
                print(f"Final Path: {' -> '.join(path)}")
                return path

            # Add neighbors to stack
            for neighbor in graph[node]:
                new_path = list(path)
                new_path.append(neighbor)
                stack.append(new_path)

    print("Goal not found.")
    return None


# RUN BOTH SEARCHES

start_node = 'A'
goal_node = 'G'

bfs(graph, start_node, goal_node)
dfs(graph, start_node, goal_node)