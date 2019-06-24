import random
import numpy
from deap import base, creator, tools, algorithms

TARGET = "Hello world!"

IND_SIZE = len(TARGET)
INT_MIN, INT_MAX = 32, 126

# type
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

# initialization
toolbox = base.Toolbox()
toolbox.register("attribute", random.randint, INT_MIN, INT_MAX)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attribute, n=IND_SIZE)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)


# operators
def evaluate(individual):
    score = 0
    for index, c in enumerate(individual):
        if chr(c) == TARGET[index]:
            score += 1
    return score,  # tuple


toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutUniformInt, low=INT_MIN, up=INT_MAX, indpb=0.1)
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("evaluate", evaluate)


def evolution():
    # create population
    pop = toolbox.population(n=500)
    CXPB, MUTPB, NGEN = 0.5, 0.2, 30

    hof = tools.HallOfFame(1)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", numpy.mean)
    stats.register("std", numpy.std)
    stats.register("min", numpy.min)
    stats.register("max", numpy.max)

    pop, log = algorithms.eaSimple(pop, toolbox, cxpb=CXPB, mutpb=MUTPB, ngen=NGEN, stats=stats, halloffame=hof,
                                   verbose=True)

    return hof.items[0]


if __name__ == "__main__":
    best = evolution()

    # print word
    word = ""
    for character in best:
        word += chr(character)
    print(word)
