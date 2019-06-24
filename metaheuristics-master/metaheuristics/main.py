from random import randint
from test_problems import ocho_alfiles,hello_world,check_diagonal,__schaffer_N2__
from problem import OptimizationProblem
from hill_climbing import hill_climbing
from simulated_annealing import simulated_annealing

alfiles = (0,0,1,5,2,1,3,4,4,6,5,3,6,7,7,2)

alfiles2 = (0,0,1,1,2,1,3,4,4,6,5,3,6,7,7,2)

problema=ocho_alfiles(alfiles2)

#for step in hill_climbing(problema, steps=10000,initial=alfiles2):
 #   print(step, ''.join(map(chr, step[0])))

for step in simulated_annealing(problema, 10, 2, delta=7, time_step=10000):
    print(step, ''.join(map(chr, step[0])))
