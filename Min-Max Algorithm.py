# Define the initial game state
initial_state = {
    'agents': ['A', 'B'],  # Agents participating in the game
    'current_agent': 'A',  # Agent starting the game
    'rewards_collected': {'A': 0, 'B': 0}  # Rewards collected by each agent
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
        successor_states.append(successor_state)
    
    return successor_states

# Define a function to evaluate the utility of a state
def evaluate(state):
    # Difference in rewards collected by agents
    return state['rewards_collected']['A'] - state['rewards_collected']['B']

# Minimax algorithm
def minimax(state, depth, maximizing_agent):
    if depth == 0 or game_over(state):
        return evaluate(state)

    if maximizing_agent:
        max_eval = float('-inf')
        for successor_state in successors(state):
            eval = minimax(successor_state, depth - 1, False)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for successor_state in successors(state):
            eval = minimax(successor_state, depth - 1, True)
            min_eval = min(min_eval, eval)
        return min_eval

# Define a function to check if the game is over
def game_over(state):
    # Check if any agent has collected all rewards
    return max(state['rewards_collected'].values()) >= 10

# Main code
winner_score = minimax(initial_state, 1, True)  # One round of the game

# Determine the winner based on the final game state
winner = 'A' if winner_score > 0 else 'B'
print("Winner of the game:", winner)
