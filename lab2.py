#  Choose a classic problem-solving task and formulate it as a search problem. Implement and compare different search
# algorithms (e.g., DFS, BFS, A*, etc.) to find solutions to the problem. Analyze the efficiency and
# effectiveness of each algorithm in solving the problem.

ROOMS = {0: [3],1: [4, 5],2: [4],3: [1, 2, 3],4: [0,3, 5],5: [1, 3]}
def bfs(start, goal):
    queue = [(start, [])]
    visited = set()
    parents = {start: None}
    while queue:
        current_node, path = queue.pop(0)
        if current_node == goal:
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
def dfs(start, goal):
    stack = [(start, [])]
    visited = set()
    parents = {start: None}
    while stack:
        current_node, path = stack.pop()
        if current_node == goal:
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
startpoint = int(input("sp: "))
goalpoint = int(input("gp: "))
searchapproach = input("method: ").upper()
if startpoint not in ROOMS or goalpoint not in ROOMS or searchapproach not in ("BFS", "DFS"):
    print("Invalid input. Please check and try again.")
    exit()
path = bfs(startpoint, goalpoint) if searchapproach == "BFS" else dfs(startpoint, goalpoint)
if path:
    print(f"Path found: {' -> '.join(map(str, path))}")
else:
    print("No path found from", startpoint, "to", goalpoint)