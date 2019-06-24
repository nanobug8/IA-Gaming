import random as rm

matriz=[[],[],[],[],[],[],[],[]]
for i in range (0,8):
    for j in range(0,8):
        matriz[i].append(rm.randint(1,8))
print (matriz)

def score (value_matrix, lista):
    score=0
    for a in range(0, 8):
        if not check_diagonal(lista, a):
            score+=(value_matrix[lista[(2 * a) + 1]][lista[2 * a]])
    return score

def ocho_alfiles (value_matrix,lista):
    return OptimizationProblem(
        domains = ((0,8),)*8,
        objective = score (value_matrix, lista),
    )