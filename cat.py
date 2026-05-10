import heapq

# A* Search Implementation
# Finds the optimal (least-cost) path from start to goal
# using f(n) = g(n) + h(n), where:
#   g(n) = actual cost from start to current node
#   h(n) = heuristic estimate from current node to goal

def a_star_search(graph, heuristics, start, goal):
    """
    A* Search Algorithm.

    Parameters:
        graph     : dict of {node: [(neighbor, cost), ...]}
        heuristics: dict of {node: estimated_cost_to_goal}
        start     : starting node
        goal      : destination node

    Returns:
        (path, total_cost) if found, else (None, infinity)
    """

    # Priority queue: stores (f_cost, g_cost, current_node, path_so_far)
    open_list = []
    heapq.heappush(open_list, (0 + heuristics[start], 0, start, [start]))

    # Tracks the minimum g(n) cost found for each visited node
    visited = {}

    while open_list:
        f, g, current, path = heapq.heappop(open_list)

        # Goal check — return path and cost when goal is reached
        if current == goal:
            return path, g

        # Skip if we've already found a cheaper path to this node
        if current in visited and visited[current] <= g:
            continue
        visited[current] = g

        # Expand neighbors
        for neighbor, cost in graph.get(current, []):
            new_g = g + cost                          # actual cost so far
            new_h = heuristics.get(neighbor, 0)       # heuristic estimate
            new_f = new_g + new_h                     # total estimated cost
            new_path = path + [neighbor]

            heapq.heappush(open_list, (new_f, new_g, neighbor, new_path))

    # No path found
    return None, float('inf')


# Graph Definition (Romania-style city map example)
# Each entry: node -> [(neighbor, travel_cost), ...]
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 6)],
    'C': [('D', 3), ('E', 5)],
    'D': [('F', 2)],
    'E': [('F', 1)],
    'F': []
}

# Heuristic values h(n): estimated straight-line distance to goal 'F'
heuristics = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 2,
    'E': 1,
    'F': 0   # Goal node always has h = 0
}

# Run A* Search
start_node = 'A'
goal_node  = 'F'

path, cost = a_star_search(graph, heuristics, start_node, goal_node)

if path:
    print(f"Optimal Path Found : {' -> '.join(path)}")
    print(f"Total Path Cost    : {cost}")
else:
    print("No path found from", start_node, "to", goal_node)