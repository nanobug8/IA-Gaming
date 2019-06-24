import random

from deap import base, creator, tools

creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()
# Attribute generator 
toolbox.register("attr_bool", random.randint, 0, 1)
# Structure initializers
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, 100)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

def evalOneMax(individual):
	return (sum(individual),)

toolbox.register("evaluate", evalOneMax)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)

CXPB = 0.5
MUTPB = 0.3

def evaluatedIndividuals(pop):
	"""Evaluate the individuals in `pop`.
	"""
	for ind in pop:
		ind.fitness.values = toolbox.evaluate(ind)
	return pop

def fitnessValues(pop):
	return [ind.fitness.values[0] for ind in pop]

def evolution():
	pop = evaluatedIndividuals(toolbox.population(n=300))
	# Extracting all the fitnesses of 
	fits = fitnessValues(pop)
	# Variable keeping track of the number of generations
	g = 0
	# Begin the evolution
	for g in range(1000):
		if max(fits) >= 100:
			break
		offspring = toolbox.select(pop, len(pop)) # Select the next generation individuals
		offspring = list(map(toolbox.clone, offspring)) # Clone the selected individuals
		# Apply crossover and mutation on the offspring
		for child1, child2 in zip(offspring[::2], offspring[1::2]):
			if random.random() < CXPB:
				toolbox.mate(child1, child2)
				del child1.fitness.values
				del child2.fitness.values
		for mutant in offspring:
			if random.random() < MUTPB:
				toolbox.mutate(mutant)
				del mutant.fitness.values
		# Evaluate the individuals with an invalid fitness
		evaluatedIndividuals(ind for ind in offspring if not ind.fitness.valid)
		pop[:] = offspring
		fits = fitnessValues(pop)

		length = len(pop)
		mean = sum(fits) / length
		sum2 = sum(x*x for x in fits)
		std = abs(sum2 / length - mean**2)**0.5

		print("Generation #%03i (%03i), min: %02.4f, avg: %02.4f, max: %02.4f, std: %02.4f." % 
			(g, length, min(fits), mean, max(fits), std))

if __name__ == '__main__':
	evolution()