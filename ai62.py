import math

def is_valid_move(grid, x, y, n, m):
    return 0 <= x < n and 0 <= y < m and grid[x][y] != 0

def get_valid_moves(grid, x, y, n, m):
    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]
    valid_moves = []

    for i in range(4):
        new_x, new_y = x + dx[i], y + dy[i]
        if is_valid_move(grid, new_x, new_y, n, m):
            valid_moves.append((new_x, new_y))
    
    return valid_moves

def calculate_cost(maze, dist, n, m, pos):
    cost = 0
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 3:
                cost += dist[i][j] - dist[pos[0]][pos[1]]
    return cost

def minimax(grid, depth, maximizingPlayer, agent1_x, agent1_y, agent2_x, agent2_y, n, m):
    if depth == 0:
        return calculate_cost(grid, [[0] * m for _ in range(n)], n, m, (agent1_x, agent1_y)) - calculate_cost(grid, [[0] * m for _ in range(n)], n, m, (agent2_x, agent2_y))

    if maximizingPlayer:
        maxEval = -math.inf
        for new_x, new_y in get_valid_moves(grid, agent1_x, agent1_y, n, m):
            maxEval = max(maxEval, minimax(grid, depth - 1, False, new_x, new_y, agent2_x, agent2_y, n, m))
        return maxEval
    else:
        minEval = math.inf
        for new_x, new_y in get_valid_moves(grid, agent2_x, agent2_y, n, m):
            minEval = min(minEval, minimax(grid, depth - 1, True, agent1_x, agent1_y, new_x, new_y, n, m))
        return minEval

def main():
    maze = [
        [2, 1, 1, 1, 0],
        [1, 0, 1, 1, 3],
        [1, 3, 1, 0, 0],
        [1, 0, 1, 1, 0],
        [3, 1, 1, 2, 3]
    ]

    n = len(maze)
    m = len(maze[0])

    # Find agent positions
    agent1_x, agent1_y = None, None
    agent2_x, agent2_y = None, None

    for i in range(n):
        for j in range(m):
            if maze[i][j] == 2:
                if agent1_x is None:
                    agent1_x, agent1_y = i, j
                else:
                    agent2_x, agent2_y = i, j

    # Play until all rewards are taken
    while any(3 in row for row in maze):
        # Determine the best move for Agent 1
        best_score = -math.inf
        best_move = None

        for new_x, new_y in get_valid_moves(maze, agent1_x, agent1_y, n, m):
            score = minimax(maze, 4, False, new_x, new_y, agent2_x, agent2_y, n, m)
            if score > best_score:
                best_score = score
                best_move = (new_x, new_y)

        # Update Agent 1 position
        if best_move is not None:
            maze[agent1_x][agent1_y] = 0  # Move Agent 1 from current position
            agent1_x, agent1_y = best_move
            maze[agent1_x][agent1_y] = 2  # Move Agent 1 to new position
        else:
            print("No valid move available for Agent 1")
            break

        # Determine the best move for Agent 2
        best_score = math.inf
        best_move = None

        for new_x, new_y in get_valid_moves(maze, agent2_x, agent2_y, n, m):
            score = minimax(maze, 4, True, agent1_x, agent1_y, new_x, new_y, n, m)
            if score < best_score:
                best_score = score
                best_move = (new_x, new_y)

        # Update Agent 2 position
        if best_move is not None:
            maze[agent2_x][agent2_y] = 0  # Move Agent 2 from current position
            agent2_x, agent2_y = best_move
            maze[agent2_x][agent2_y] = 2  # Move Agent 2 to new position
        else:
            print("No valid move available for Agent 2")
            break

        # Print positions of both agents after each turn
        print("Agent 1 position:", (agent1_x, agent1_y))
        print("Agent 2 position:", (agent2_x, agent2_y))

        # Remove reward from maze if agents have reached it
        if maze[agent1_x][agent1_y] == 3:
            maze[agent1_x][agent1_y] = 0
        if maze[agent2_x][agent2_y] == 3:
            maze[agent2_x][agent2_y] = 0

    # Calculate cost for both agents after all rewards are taken
    cost_agent1 = calculate_cost(maze, [[0] * m for _ in range(n)], n, m, (agent1_x, agent1_y))
    cost_agent2 = calculate_cost(maze, [[0] * m for _ in range(n)], n, m, (agent2_x, agent2_y))

    # Determine the winner
    if cost_agent1 < cost_agent2:
        print("Agent 1 wins with {} steps".format(cost_agent1))
    elif cost_agent2 < cost_agent1:
        print("Agent 2 wins with {} steps".format(cost_agent2))
    else:
        print("It's a tie!")

if __name__ == "__main__":
    main()
