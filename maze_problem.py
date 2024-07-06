import heapq


class Maze:
    def __init__(self, size, start, goal, obstacles):
        self.size = size
        self.start = start
        self.goal = goal
        self.obstacles = obstacles

    def is_valid_move(self, position):
        x, y = position
        return 1 <= x <= self.size[0] and 1 <= y <= self.size[1] and position not in self.obstacles

    def get_neighbors(self, position):
        x, y = position
        neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        return [neighbor for neighbor in neighbors if self.is_valid_move(neighbor)]


def dfs(maze):
    stack = [(maze.start, [maze.start])]
    visited = set()

    while stack:
        current, path = stack.pop()
        if current == maze.goal:
            return path
        if current not in visited:
            visited.add(current)
            for neighbor in maze.get_neighbors(current):
                stack.append((neighbor, path + [neighbor]))
    return None


def bfs(maze):
    queue = [(maze.start, [maze.start])]
    visited = set()

    while queue:
        current, path = queue.pop(0)
        if current == maze.goal:
            return path
        if current not in visited:
            visited.add(current)
            for neighbor in maze.get_neighbors(current):
                queue.append((neighbor, path + [neighbor]))
    return None


def dls(maze, depth_limit):
    stack = [(maze.start, [maze.start], 0)]
    visited = set()

    while stack:
        current, path, depth = stack.pop()
        if current == maze.goal:
            return path
        if depth < depth_limit and current not in visited:
            visited.add(current)
            for neighbor in maze.get_neighbors(current):
                stack.append((neighbor, path + [neighbor], depth + 1))
    return None


def ucs(maze):
    # Uniform Cost Search using heapq
    heap = [(0, maze.start, [maze.start])]
    visited = set()

    while heap:
        cost, current, path = heapq.heappop(heap)
        if current == maze.goal:
            return path
        if current not in visited:
            visited.add(current)
            for neighbor in maze.get_neighbors(current):
                new_cost = cost + 1  # Assuming cost of each move is 1
                heapq.heappush(heap, (new_cost, neighbor, path + [neighbor]))
    return None


def gbfs(maze):
    # Greedy Best First Search
    queue = [(heuristic(maze.start, maze.goal), maze.start, [maze.start])]
    visited = set()

    while queue:
        _, current, path = heapq.heappop(queue)
        if current == maze.goal:
            return path
        if current not in visited:
            visited.add(current)
            for neighbor in maze.get_neighbors(current):
                heapq.heappush(queue, (heuristic(neighbor, maze.goal), neighbor, path + [neighbor]))
    return None


def astar(maze):
    queue = [(heuristic(maze.start, maze.goal), 0, maze.start, [maze.start])]
    visited = set()

    while queue:
        _, cost, current, path = heapq.heappop(queue)
        if current == maze.goal:
            return path
        if current not in visited:
            visited.add(current)
            for neighbor in maze.get_neighbors(current):
                new_cost = cost + 1  # Assuming cost of each move is 1
                heapq.heappush(queue,
                               (new_cost + heuristic(neighbor, maze.goal), new_cost, neighbor, path + [neighbor]))
    return None


def heuristic(current, goal):
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])


def read_input(file_path):
    with open(file_path, 'r') as file:
        size = tuple(map(int, file.readline().strip().split(',')))
        start, goal = map(tuple, [map(int, coord.split(',')) for coord in file.readline().strip().split(';')])
        obstacles = [tuple(map(int, coord.split(','))) for coord in file.readline().strip().split(';')]
        method = file.readline().strip()
    return size, start, goal, obstacles, method


def main():
    size, start, goal, obstacles, method = read_input("input.txt")
    maze = Maze(size, start, goal, obstacles)

    if method == "dfs":
        print("Approach Defth First Search :  \nBlocks Travelled ", dfs(maze))
    elif method == "bfs":
        print("Approach Breadth First Search :  \nBlocks Travelled ", bfs(maze))
    elif method == "dls":
        print("Approach Depth Limit Search(upto 3) :  \nBlocks Travelled ", dls(maze, depth_limit=3))
    elif method == "ucs":
        print("Approach Uniform Cost Search :  \nBlocks Travelled ", ucs(maze))
    elif method == "gbfs":
        print("Approach Greedy Breadth First Search :  \nBlocks Travelled ", gbfs(maze))
    elif method == "astar":
        print("Approach Astar :  \nBlocks Travelled ", astar(maze))
    else:
        print("Invalid search strategy.")


if __name__ == "__main__":
    main()
