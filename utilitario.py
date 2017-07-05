import numpy as np

def distancia(a, b):
    return ((a - b) ** 2) ** (1/2)


def som_matriz(a, b):
    r = []
    for i in range(len(a)):
        linha = []
        for j in range(len(a[0])):
            linha.append(a[i][j] + b[i][j])
        r.append(linha)
    return r

def sub_matriz(a, b):
    r = []
    for i in range(len(a)):
        linha = []
        for j in range(len(a[0])):
            linha.append(a[i][j] - b[i][j])
        r.append(linha)
    return r
