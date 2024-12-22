import random

POPULATION_SIZE = 100
NUM_ITEMS = 8
MUTATION_RATE = 0.01
CROSSOVER_RATE = 0.7
GENERATIONS = 1000
MAX_WEIGHT = 15

weights = [2, 3, 4, 5, 9, 7, 3, 6]
values = [1, 4, 5, 7, 10, 6, 2, 8]

def generate_individual(num_items):
    return [random.randint(0, 1) for _ in range(num_items)]

def fitness(individual):

    total_value = sum(individual[i] * values[i] for i in range(NUM_ITEMS))
    total_weight = sum(individual[i] * weights[i] for i in range(NUM_ITEMS))
    if total_weight > MAX_WEIGHT:
        return 0  # We can not exceed a specified weight
    return total_value

def select(population):
   #Roulette Wheel Selection
    total_fitness = sum(fitness(ind) for ind in population)
    pick = random.uniform(0, total_fitness)
    current = 0
    for ind in population:
        current += fitness(ind)
        if current > pick:
            return ind

def crossover(parent1, parent2):

    if random.random() < CROSSOVER_RATE:
        point = random.randint(1, NUM_ITEMS - 1)
        return (parent1[:point] + parent2[point:], parent2[:point] + parent1[point:])
    return parent1, parent2

def mutate(individual):
    return [bit if random.random() > MUTATION_RATE else 1 - bit for bit in individual]

def genetic_algorithm():

    population = [generate_individual(NUM_ITEMS) for _ in range(POPULATION_SIZE)]

    for generation in range(GENERATIONS):

        population = sorted(population, key=fitness, reverse=True)

        if fitness(population[0]) > 0:
            #If you only want to see the final best solution, just remove this line and wait for a few mins since generation size is 1000 or just lower generation size to 100 
            print(f"Generation {generation}: Best fitness = {fitness(population[0])}")

        next_generation = []

        # Elitism
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
    print(f"Best solution: {best_individual} with value {fitness(best_individual)}")


genetic_algorithm()