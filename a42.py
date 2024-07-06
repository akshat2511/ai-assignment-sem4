import heapq

def is_valid_move(maze, position):
    x, y = position
    return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] != 1

def get_neighbors(position):
    x, y = position
    return [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]

def heuristic(position, goals):
    return min(abs(position[0] - goal[0]) + abs(position[1] - goal[1]) for goal in goals)

def astar(maze, start, goals):
    visited = set()
    pq = [(heuristic(start, goals), start, 0, [])]
    
    while pq:
        _, current_position, cost, path = heapq.heappop(pq)
        
        if current_position in visited:
            continue
        
        visited.add(current_position)
        path.append(current_position)
        
        if maze[current_position[0]][current_position[1]] == 3:
            return path, cost
        
        for neighbor in get_neighbors(current_position):
            if is_valid_move(maze, neighbor) and neighbor not in visited:
                new_cost = cost + 1
                heapq.heappush(pq, (new_cost + heuristic(neighbor, goals), neighbor, new_cost, path.copy()))
    
    return [], -1

def read_maze(file_path):
    with open(file_path, 'r') as file:
        maze = [list(map(int, line.strip().split())) for line in file]
    return maze

def write_output(file_path, path, steps):
    with open(file_path, 'w') as file:
        for position in path:
            file.write(f"{position[0]},{position[1]}\n")
        file.write(f"Steps: {steps}\n")

if __name__ == "__main__":
    maze_file = "maze.txt"
    output_file = "out_astar.txt"

    maze = read_maze(maze_file)

    start = None
    goals = []

    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 2:
                start = (i, j)
            elif maze[i][j] == 3:
                goals.append((i, j))

    path, steps = astar(maze, start, goals)

    write_output(output_file, path, steps)
