import sys
from queue import Queue, LifoQueue, PriorityQueue

def read_input(file_path):
    with open(file_path, 'r') as file:
        size = tuple(map(int, file.readline().strip().split(',')))
        start, goal = map(lambda s: tuple(map(int, s.split(','))), file.readline().strip().split(';'))
        obstacles = [tuple(map(int, line.split(','))) for line in file.readline().strip().split(';')]
        strategy = file.readline().strip()
    return size, start, goal, obstacles, strategy



def write_output(file_path, explored_sequence, total_cost):
    with open(file_path, 'w') as file:
        for block in explored_sequence:
            file.write(f"{block[0]},{block[1]}\n")
        file.write(f"Total Cost: {total_cost}\n")

def is_valid_move(size, position, obstacles):
    x, y = position
    return 1 <= x <= size[0] and 1 <= y <= size[1] and position not in obstacles

def get_neighbors(position):
    x, y = position
    return [(x-1, y), (x, y-1), (x+1, y), (x, y+1)]

def dfs(size, start, goal, obstacles):
    visited = set()
    stack = LifoQueue()
    stack.put(start)
    explored_sequence = []
    total_cost = 0

    while not stack.empty():
        current_position = stack.get()

        if current_position == goal:
            explored_sequence.append(current_position)
            return explored_sequence, total_cost

        if current_position not in visited:
            visited.add(current_position)
            explored_sequence.append(current_position)

            for neighbor in get_neighbors(current_position):
                if is_valid_move(size, neighbor, obstacles) and neighbor not in visited:
                    stack.put(neighbor)
                    total_cost += 1

    return explored_sequence, total_cost

def bfs(size, start, goal, obstacles):
    visited = set()
    queue = Queue()
    queue.put(start)
    explored_sequence = []
    total_cost = 0

    while not queue.empty():
        current_position = queue.get()

        if current_position == goal:
            explored_sequence.append(current_position)
            return explored_sequence, total_cost

        if current_position not in visited:
            visited.add(current_position)
            explored_sequence.append(current_position)

            for neighbor in get_neighbors(current_position):
                if is_valid_move(size, neighbor, obstacles) and neighbor not in visited:
                    queue.put(neighbor)
                    total_cost += 1

    return explored_sequence, total_cost

def dls(size, start, goal, obstacles, depth_limit):
    visited = set()
    stack = LifoQueue()
    stack.put((start, 0))
    explored_sequence = []

    while not stack.empty():
        current_position, current_depth = stack.get()

        if current_position == goal:
            explored_sequence.append(current_position)
            return explored_sequence, current_depth

        if current_depth < depth_limit and current_position not in visited:
            visited.add(current_position)
            explored_sequence.append(current_position)

            for neighbor in get_neighbors(current_position):
                if is_valid_move(size, neighbor, obstacles) and neighbor not in visited:
                    stack.put((neighbor, current_depth + 1))

    return explored_sequence, -1  # Goal not reached within depth limit

def ucs(size, start, goal, obstacles):
    visited = set()
    pq = PriorityQueue()
    pq.put((0, start))
    explored_sequence = []

    while not pq.empty():
        current_cost, current_position = pq.get()

        if current_position == goal:
            explored_sequence.append(current_position)
            return explored_sequence, current_cost

        if current_position not in visited:
            visited.add(current_position)
            explored_sequence.append(current_position)

            for neighbor in get_neighbors(current_position):
                if is_valid_move(size, neighbor, obstacles) and neighbor not in visited:
                    new_cost = current_cost + 1
                    pq.put((new_cost, neighbor))

    return explored_sequence, -1  # Goal not reachable

def heuristic(position, goal):
    return abs(position[0] - goal[0]) + abs(position[1] - goal[1])

def gbfs(size, start, goal, obstacles):
    visited = set()
    pq = PriorityQueue()
    pq.put((heuristic(start, goal), start))
    explored_sequence = []

    while not pq.empty():
        _, current_position = pq.get()

        if current_position == goal:
            explored_sequence.append(current_position)
            return explored_sequence, heuristic(current_position, goal)

        if current_position not in visited:
            visited.add(current_position)
            explored_sequence.append(current_position)

            for neighbor in get_neighbors(current_position):
                if is_valid_move(size, neighbor, obstacles) and neighbor not in visited:
                    pq.put((heuristic(neighbor, goal), neighbor))

    return explored_sequence, -1  # Goal not reachable

def astar(size, start, goal, obstacles):
    visited = set()
    pq = PriorityQueue()
    pq.put((heuristic(start, goal), 0, start))
    explored_sequence = []

    while not pq.empty():
        _, current_cost, current_position = pq.get()

        if current_position == goal:
            explored_sequence.append(current_position)
            return explored_sequence, current_cost

        if current_position not in visited:
            visited.add(current_position)
            explored_sequence.append(current_position)

            for neighbor in get_neighbors(current_position):
                if is_valid_move(size, neighbor, obstacles) and neighbor not in visited:
                    new_cost = current_cost + 1
                    pq.put((new_cost + heuristic(neighbor, goal), new_cost, neighbor))

    return explored_sequence, -1  # Goal not reachable

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py input.txt output.txt")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    size, start, goal, obstacles, strategy = read_input(input_file)

    if strategy == 'dfs':
        explored_sequence, total_cost = dfs(size, start, goal, obstacles)
    elif strategy == 'bfs':
        explored_sequence, total_cost = bfs(size, start, goal, obstacles)
    elif strategy == 'dls':
        explored_sequence, total_cost = dls(size, start, goal, obstacles, depth_limit=3)
    elif strategy == 'ucs':
        explored_sequence, total_cost = ucs(size, start, goal, obstacles)
    elif strategy == 'gbfs':
        explored_sequence, total_cost = gbfs(size, start, goal, obstacles)
    elif strategy == 'astar':
        explored_sequence, total_cost = astar(size, start, goal, obstacles)
    else:
        print("Invalid search strategy.")
        sys.exit(1)

    write_output(output_file, explored_sequence, total_cost)
