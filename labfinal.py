import random

def create_board(size):
    board = [0] * size
    for i in range(size):
        board[i] = random.randint(0, size - 1)
    return board

def fitness(board):
    conflicts = 0
    size = len(board)
    for i in range(size):
        for j in range(i + 1, size):
            if board[i] == board[j] or abs(i - j) == abs(board[i] - board[j]):
                conflicts += 1
    return conflicts

def crossover(parent1, parent2):
    size = len(parent1)
    crossover_point = random.randint(1, size - 1)
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child

def mutate(board):
    size = len(board)
    mutation_point = random.randint(0, size - 1)
    new_value = random.randint(0, size - 1)
    board[mutation_point] = new_value
    return board

def genetic_algorithm(population_size, generations):
    board_size = 5
    population = [create_board(board_size) for _ in range(population_size)]

    for _ in range(generations):
        population = sorted(population, key=lambda x: fitness(x))
        if fitness(population[0]) == 0:
            return population[0]

        new_population = []

        for _ in range(population_size // 2):
            parent1 = random.choice(population[:population_size // 2])
            parent2 = random.choice(population[:population_size // 2])
            child = crossover(parent1, parent2)
            if random.random() < 0.1:
                child = mutate(child)
            new_population.append(child)

        population = new_population

    return None

solution = genetic_algorithm(population_size=100, generations=1000)
if solution:
    print("Solution found:", solution)
else:
    print("Solution not found. Try increasing the population size or number of generations.")