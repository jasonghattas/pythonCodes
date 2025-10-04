import random
import string
user_pass = input("Enter Your Password: ")

def generate_word(length):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

def fitness(word, target):
    # How many letters are correct and in the right position
    return sum(1 for a, b in zip(word, target) if a == b)

def mutate(word, mutation_rate=0.1):
    # Randomly change letters with small probability
    new_word = ''
    for ch in word:
        if random.random() < mutation_rate:
            new_word += random.choice(string.ascii_lowercase)
        else:
            new_word += ch
    return new_word

def crossover(parent1, parent2):
    # Mix two words
    split = random.randint(0, len(parent1) - 1)
    return parent1[:split] + parent2[split:]

def genetic_search(target, population_size=200):
    population = [generate_word(len(target)) for _ in range(population_size)]
    generation = 0

    while True:
        generation += 1
        population = sorted(population, key=lambda w: -fitness(w, target))
        best = population[0]
        print(f"Gen {generation}: {best} (tries: {fitness(best, target)})")
        
        if best == target:
            print(f"✅ Found '{target}' in {generation} tries!")
            break
        
        # Keep top 20%
        survivors = population[:population_size // 5]
        
        # Create new generation from survivors
        new_population = survivors.copy()
        while len(new_population) < population_size:
            p1, p2 = random.sample(survivors, 2)
            child = crossover(p1, p2)
            child = mutate(child)
            new_population.append(child)
        population = new_population
genetic_search(user_pass)
