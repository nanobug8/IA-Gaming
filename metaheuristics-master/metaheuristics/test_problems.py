""" # Test functions

Test functions for benchmarking optimization techniques.
"""
from math import sin, inf
from random import randint

from problem import OptimizationProblem


def hello_world(target_str="Hello world!"):
    target_chars = tuple(map(ord, target_str))
    print(str(target_chars))
    return OptimizationProblem(
        domains=((32, 126),) * len(target_str),
        objective=lambda chars: sum(abs(c - t) for (c, t) in zip(chars, target_chars))
    )


# References:
# + [Test functions for optimization @ Wikipedia](https://en.wikipedia.org/wiki/Test_functions_for_optimization)
# + [Test functions and datasets @ Virtual Library of Simulation Experiments](https://www.sfu.ca/~ssurjano/optimization.html)

def __schaffer_N2__(elem):
    (x, y) = elem
    return 0.5 + (sin(x * x - y * y) ** 2 - 0.5) / ((1 + 0.001 * (x * x + y * y)) ** 2)


SCHAFFER_N2 = OptimizationProblem(domains=((-100, +100),) * 2, objective=__schaffer_N2__)


def check_diagonal(lista, indice_alfil):
    comparte = False
    x = lista[2 * indice_alfil]
    y = lista[(2 * indice_alfil) + 1]
    while not comparte:
        for otro_alfil in range(0, 8):
            if otro_alfil != indice_alfil:
                x_2 = lista[2 * otro_alfil]
                y_2 = lista[(2 * otro_alfil) + 1]
                if abs(x - x_2) == abs(y - y_2):
                    comparte = True
        break
    return comparte


# funcion objetivo, da el puntaje de cada posicion
def __score__(lista):
    score = 0
    matriz = [[], [], [], [], [], [], [], []]
    for i in range(0, 8):
        for j in range(0, 8):
            matriz[i].append(randint(0, 8))
    for a in range(0, 4):
        if not check_diagonal(lista, a):
            x = lista[(2*a)+1]
            y = lista[2*a]
            score += (matriz[x][y])
    return score


def ocho_alfiles(lista):
    return OptimizationProblem(
        domains=((0, 7),) * 16,
        objective=__score__,
        target=inf
    )
