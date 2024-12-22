import random

# Genetic Algorithm Parameters
POPULATION_SIZE = 100
BOARD_SIZE = 8
MUTATION_RATE = 0.05
CROSSOVER_RATE = 0.8
GENERATIONS = 1000

def generate_individual(board_size):
    return [random.randint(0, board_size - 1) for _ in range(board_size)]

def fitness(individual):
    non_attacking_pairs = 0
    for i in range(len(individual)):
        for j in range(i + 1, len(individual)):
            #considers to be a non attacking pair if not in same column and if not in same diagonal
            if individual[i] != individual[j] and abs(individual[i] - individual[j]) != abs(i - j):
                non_attacking_pairs += 1
    return non_attacking_pairs

def select(population):
 
    total_fitness = sum(fitness(ind) for ind in population)
    pick = random.uniform(0, total_fitness)
    current = 0
    for ind in population:
        current += fitness(ind)
        if current > pick:
            return ind

def crossover(parent1, parent2):

    if random.random() < CROSSOVER_RATE:
        point = random.randint(1, BOARD_SIZE - 1)
        return (parent1[:point] + parent2[point:], parent2[:point] + parent1[point:])
    return parent1, parent2

def mutate(individual):

    for i in range(len(individual)):
        if random.random() < MUTATION_RATE:
            individual[i] = random.randint(0, BOARD_SIZE - 1)
    return individual

def genetic_algorithm():

    population = [generate_individual(BOARD_SIZE) for _ in range(POPULATION_SIZE)]

   #combination formula i.e. n(n-1)/2
    max_possible_fitness = (BOARD_SIZE * (BOARD_SIZE - 1)) // 2  

    for generation in range(GENERATIONS):

        population = sorted(population, key=fitness, reverse=True)

        if fitness(population[0]) == max_possible_fitness:
            print(f"Solution found in generation {generation}: {population[0]} with fitness {fitness(population[0])}")
            return

        next_generation = []

        next_generation.append(population[0])

        while len(next_generation) < POPULATION_SIZE:
            parent1 = select(population)
            parent2 = select(population)
            offspring1, offspring2 = crossover(parent1, parent2)
            next_generation.append(mutate(offspring1))
            if len(next_generation) < POPULATION_SIZE:
                next_generation.append(mutate(offspring2))

        population = next_generation

    best_individual = max(population, key=fitness)
    print(f"Best solution found after {GENERATIONS} generations: {best_individual} with fitness {fitness(best_individual)}")

genetic_algorithm()
