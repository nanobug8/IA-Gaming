from adversarial_search.KMA import *
from adversarial_search.agents.random import RandomAgent
from adversarial_search.agents.mcts import MCTSAgent
from adversarial_search import parameters
import random
import numpy
from deap import base, creator, tools, algorithms



TURN_TARGET = 18

INT_MIN, INT_MAX = 1,30

    # type
creator.create("FitnessMulti", base.Fitness, weights=(-1.0,-1.0))
creator.create("Individual", list, fitness=creator.FitnessMulti)

    # initialization
toolbox = base.Toolbox()
toolbox.register("attribute", random.randint, INT_MIN, INT_MAX)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attribute, n=12)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)


    # operators
def evaluate(individual):
    n_simulations = 100
    penalty = 0
    if individual[8]>9:
        penalty += 500
    if individual[11]>9:
        penalty += 500
    win_ratio = 0
    agent0 = RandomAgent(name='Player 0')
    agent00 = RandomAgent(name='Player 00')
    total_turns = 0
    PARAM.set_parameters(individual[0],individual[1],individual[2],individual[3],individual[4],individual[5],individual[6],individual[7],individual[8],individual[9],individual[10],individual[11])
    for i in range(n_simulations):
        game = KMA()
        turns = 0
        for move_number, moves, game_state in match(game, agent0, agent00):
            if move_number is not None:
                turns += 1
            else:
                if moves['Good']<0:
                    win_ratio-=1
                else:
                    win_ratio+=1
                total_turns+=turns
    return abs(win_ratio)+penalty,  abs((total_turns/n_simulations)-TURN_TARGET)+penalty


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

    print(best)