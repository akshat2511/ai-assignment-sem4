# Define the initial game state
initial_state = {
    'agents': ['A', 'B'],  # Agents participating in the game
    'current_agent': 'A',  # Agent starting the game
    'rewards_collected': {'A': 0, 'B': 0},  # Rewards collected by each agent
    'visiting_sequence': []  # Visiting sequence for each agent
}

# Define a function to generate successor states
def successors(state):
    current_agent = state['current_agent']
    next_agent = 'A' if current_agent == 'B' else 'B'
    
    # Generate successor states for the current agent's turn
    successor_states = []
    for reward in range(1, 11):
        successor_state = state.copy()
        successor_state['rewards_collected'][current_agent] += reward
        successor_state['current_agent'] = next_agent
        successor_state['visiting_sequence'].append((current_agent, reward))
        successor_states.append(successor_state)
    
    return successor_states

# Define a function to evaluate the utility of a state
def evaluate(state):
    # Difference in rewards collected by agents
    return state['rewards_collected']['A'] - state['rewards_collected']['B']

# Alpha-beta algorithm
def alpha_beta(state, depth, alpha, beta, maximizing_agent):
    if depth == 0 or game_over(state):
        return evaluate(state)

    if maximizing_agent:
        max_eval = float('-inf')
        for successor_state in successors(state):
            eval = alpha_beta(successor_state, depth - 1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  # Beta cutoff
        return max_eval
    else:
        min_eval = float('inf')
        for successor_state in successors(state):
            eval = alpha_beta(successor_state, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break  # Alpha cutoff
        return min_eval

# Define a function to check if the game is over
def game_over(state):
    # Check if any agent has collected all rewards
    return max(state['rewards_collected'].values()) >= 10

# Main code
winner_score = alpha_beta(initial_state, 3, float('-inf'), float('inf'), True)  # Search depth: 3

# Determine the winner based on the final game state
winner = 'A' if winner_score > 0 else 'B'
print("Winner of the game:", winner)
print("Visiting sequence for each agent:", initial_state['visiting_sequence'])
