import heapq

class MazeSolver:
    def __init__(self, maze):
        self.maze = maze
        self.rows = len(maze)
        self.cols = len(maze[0])
        self.start = self.find_start()
        self.rewards = self.find_rewards()
        self.visited = set()

    def find_start(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.maze[i][j] == 2:
                    return (i, j)

    def find_rewards(self):
        rewards = []
        for i in range(self.rows):
            for j in range(self.cols):
                if self.maze[i][j] == 3:
                    rewards.append((i, j))
        return rewards

    def heuristic(self, current, goal):
        return abs(current[0] - goal[0]) + abs(current[1] - goal[1])

    def is_valid_move(self, position):
        x, y = position
        return 0 <= x < self.rows and 0 <= y < self.cols and self.maze[x][y] != 1 and position not in self.visited

    def astar(self, start, goal):
        heap = [(0, start, [])]

        while heap:
            _, current, path = heapq.heappop(heap)

            if current == goal:
                self.visited.update(path)
                return path

            if current not in self.visited:
                self.visited.add(current)

                moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

                for move in moves:
                    next_position = (current[0] + move[0], current[1] + move[1])
                    if self.is_valid_move(next_position):
                        heapq.heappush(heap, (self.heuristic(next_position, goal) + len(path), next_position, path + [next_position]))

        return []

    def solve_maze(self):
        start = self.start
        total_steps = 0

        for reward in self.rewards:
            path = self.astar(start, reward)
            total_steps += len(path) - 1
            start = reward

        return total_steps

    def write_output(self, filename):
        with open(filename, 'w') as file:
            for position in sorted(self.visited):
                file.write(f"{position[0]},{position[1]}\n")


if __name__ == "__main__":
    maze = [
        [2, 0, 0, 0, 1],
        [0, 1, 0, 0, 3],
        [0, 3, 0, 1, 1],
        [0, 1, 0, 0, 1],
        [3, 0, 0, 0, 3]
    ]

    solver = MazeSolver(maze)
    total_steps = solver.solve_maze()

    print("Total Steps:", total_steps)
    solver.write_output("out_astar.txt")
