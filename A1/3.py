ROOMS = {
    0: [4],
    1: [3, 5],
    2: [3],
    3: [1, 2, 4],
    4: [0,3, 5],
    5: [1, 4]
}

def breadth_first_search(start, goal):
    queue = [(start, [])]
    visited = set()
    parents = {start: None}

    while queue:
        current_node, path = queue.pop(0)

        if current_node == goal:
            # Reconstruct the path using parents
            final_path = []
            while current_node is not None:
                final_path.insert(0, current_node)
                current_node = parents[current_node]
            return final_path

        if current_node not in visited:
            visited.add(current_node)
            for neighbor in ROOMS[current_node]:
                if neighbor not in visited and neighbor not in parents:
                    parents[neighbor] = current_node
                    queue.append((neighbor, path + [current_node]))

    return None

def depth_first_search(start, goal):
    stack = [(start, [])]
    visited = set()
    parents = {start: None}

    while stack:
        current_node, path = stack.pop()

        if current_node == goal:
            # Reconstruct the path using parents
            final_path = []
            while current_node is not None:
                final_path.insert(0, current_node)
                current_node = parents[current_node]
            return final_path

        if current_node not in visited:
            visited.add(current_node)
            for neighbor in ROOMS[current_node]:
                if neighbor not in visited and neighbor not in parents:
                    parents[neighbor] = current_node
                    stack.append((neighbor, path + [current_node]))

    return None

start_point = int(input("Enter the starting point (0-5): "))
goal_point = int(input("Enter the goal point (0-5): "))
search_approach = input("Choose search approach (BFS or DFS): ").upper()

if start_point not in ROOMS or goal_point not in ROOMS or search_approach not in ("BFS", "DFS"):
    print("Invalid input. Please check and try again.")
    exit()

path = breadth_first_search(start_point, goal_point) if search_approach == "BFS" else depth_first_search(start_point, goal_point)

if path:
    print(f"Path found: {' -> '.join(map(str, path))}")
else:
    print("No path found from", start_point, "to", goal_point)