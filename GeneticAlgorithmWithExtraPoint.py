import random

good_attributes = {
    'Honesty': 10,
    'Perseverance': 9,
    'Loyalty': 8,
    'Respect': 7,
    'Punctual': 6,
    'Trustworthy': 5
}

bad_attributes = {
    'Lie': -3,
    'Lazy': -1,
    'Racism': -2,
    'Addiction': -4,
    'SpendThrift': -7,
    'Deception': -8
}

population_size = 100
gene_count = 7

def create_chromosome():
    all_genes = list(good_attributes.keys()) + list(bad_attributes.keys())
    chromosome = random.sample(all_genes, gene_count)
    return chromosome

population = []
for _ in range(population_size):
    chromosome = create_chromosome()
    population.append(chromosome)

def fitness(chromosome):
  score = 0
  genes = dict()

  for gene in chromosome:
    if gene in good_attributes:  
      score += good_attributes[gene]
      genes[gene] = 1
    elif gene in bad_attributes:  
      score += bad_attributes[gene]  
      genes[gene] = -1

  return score + sum(genes.values())

def selection(population):
    population.sort(key=lambda chromosome: fitness(chromosome), reverse=True)
    return population[:int(len(population) * 0.1)]

def crossover(chromosome1, chromosome2):
    crossover_point = random.randint(1, gene_count - 1)
    first_half = chromosome1[:crossover_point]
    second_half = [gene for gene in chromosome2 if gene not in first_half]
    new_chromosome = first_half + second_half[:gene_count - len(first_half)]
    return new_chromosome

def mutation(chromosome):
    mutated_chromosome = chromosome.copy()
    for _ in range(int(len(chromosome) * 0.1)):
        gene_index = random.randint(0, gene_count - 1)
        all_genes = list(good_attributes.keys()) + list(bad_attributes.keys())
        new_genes = [gene for gene in all_genes if gene not in mutated_chromosome]
        mutated_chromosome[gene_index] = random.choice(new_genes)
    return mutated_chromosome


def generate_new_generation(population):
    new_generation = population.copy()
    selected_parents = selection(population)
    for _ in range(int(population_size * 0.1)):
        parent1 = random.choice(selected_parents)
        parent2 = random.choice(selected_parents)
        child = crossover(parent1, parent2)
        new_generation.append(child)
        for _ in range(int(population_size * 0.1)):
            chromosome = random.choice(population)
            mutated_chromosome = mutation(chromosome)
            new_generation.append(mutated_chromosome)
            return new_generation

num_generations = 50
for generation in range(num_generations):
    population = generate_new_generation(population)
    if (generation + 1) % 10 == 0:
        print(f"Generation {generation + 1}:")
        for chromosome in population[:int(population_size * 0.1)]:
            print("Chromosome:", chromosome)
            print("Fitness Score:", fitness(chromosome))
            print()

best_chromosome = max(population, key=lambda chromosome: fitness(chromosome))

print("Best Chromosome:", best_chromosome)
print("Best Chromosome Score:", fitness(best_chromosome))
