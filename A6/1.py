import heapq

class MazeSolver:
    def __init__(self, maze):
        self.maze = maze
        self.rows = len(maze)
        self.cols = len(maze[0])
        self.agent_A_start = self.find_start(2)
        self.agent_B_start = self.find_start(4)
        self.rewards = self.find_rewards()
        self.visited_A = set()
        self.visited_B = set()

    def find_start(self, agent_id):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.maze[i][j] == agent_id:
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
        return 0 <= x < self.rows and 0 <= y < self.cols and self.maze[x][y] != 1

    def astar(self, start, goal, visited):
        heap = [(0, start, [])]

        while heap:
            _, current, path = heapq.heappop(heap)

            if current == goal:
                visited.update(path)
                return path

            if current not in visited:
                visited.add(current)

                moves = [(-1, 0, 'U'), (1, 0, 'D'), (0, -1, 'L'), (0, 1, 'R')]

                for dx, dy, action in moves:
                    next_position = (current[0] + dx, current[1] + dy)
                    if self.is_valid_move(next_position):
                        heapq.heappush(heap, (self.heuristic(next_position, goal) + len(path), next_position, path + [(next_position, action)]))

        return []

    def solve_maze(self, agent_start, agent_rewards, visited_set):
        start = agent_start
        total_steps = 0

        for reward in agent_rewards:
            path = self.astar(start, reward, visited_set)
            total_steps += len(path) - 1
            start = reward

        return total_steps

    def play_game(self):
        wins_A = 0
        wins_B = 0

        for _ in range(10):
            steps_A = self.solve_maze(self.agent_A_start, self.rewards, self.visited_A)
            steps_B = self.solve_maze(self.agent_B_start, self.rewards, self.visited_B)

            if steps_A < steps_B:
                wins_A += 1
            else:
                wins_B += 1

            print(f"Round {_ + 1}:")
            print(f"Agent A steps: {steps_A}")
            print(f"Agent B steps: {steps_B}")
            print()

        # Declare the winner of all rounds combined
        if wins_A > wins_B:
            print("Agent A is the winner!")
        elif wins_B > wins_A:
            print("Agent B is the winner!")
        else:
            print("It's a tie!")

if __name__ == "__main__":
    maze = [
        [2, 0, 0, 0, 1],
        [0, 1, 0, 0, 3],
        [0, 3, 0, 1, 1],
        [0, 1, 0, 0, 1],
        [3, 0, 0, 0, 4]
    ]

    solver = MazeSolver(maze)
    solver.play_game()
