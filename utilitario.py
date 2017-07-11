import numpy as np

def distancia(a, b):
    return a - b

def dist_eclidiana(a, b):
    return ((a[0] - b[0])**2 + (a[1] - b[1])**2)**(1/2)

def most_common(lst):
    return max(set(lst), key = lst.count)

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
