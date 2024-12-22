import random

LENGTH= 8
POPULATION_SIZE=100
MUTATION_RATE=0.01
CROSSOVER_RATE= 0.7
GENERATIONS=1000

def generate_individual(length):
    return [random.randint(0,1) for _ in range(length)]

def fitness(individual):
    return sum(individual)

#Roulette Wheel Selection
def select_individual(population):
    total_fitness= sum(fitness(ind) for ind in population)

    pick= random.uniform(0, total_fitness)

    current=0
    for ind in population:
        current+= fitness(ind)

        if(current>pick):
            return ind

def crossover(parent1, parent2):
    val= random.random()
    if val<CROSSOVER_RATE:
        splitting_point= random.randint(1,LENGTH-1)

        return (parent1[:splitting_point]+ parent2[splitting_point:],parent2[:splitting_point]+ parent1[splitting_point:] )
    
    return parent1, parent2

def mutation(individual):

    return [bit if random.random() > MUTATION_RATE else 1-bit for bit in individual ]

def genetic_algorithm():

    population= [generate_individual(LENGTH) for _ in range (POPULATION_SIZE)]

    for generation in range(GENERATIONS):
        population= sorted(population, key=fitness, reverse=True)

        if fitness(population[0])==LENGTH:
            print(f"Solution found in generation:{generation}: {population[0]} ")
            return
        
        next_generation=[]
        next_generation.append(population[0])

        while len(next_generation)<POPULATION_SIZE:
            parent1= select_individual(population)
            parent2= select_individual(population)

            offspring1,offspring2= crossover(parent1, parent2)

            next_generation.append(mutation(offspring1))

            if len(next_generation)<POPULATION_SIZE:
                next_generation.append(mutation(offspring2))

        population= next_generation

    print("Solution not found in this generation")

genetic_algorithm()
    
