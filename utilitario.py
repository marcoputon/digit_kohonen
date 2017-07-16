import numpy as np


'''
Função de distância euclidiana entre dois pontos.
'''
def dist_eclidiana(a, b):
    return ((a[0] - b[0])**2 + (a[1] - b[1])**2)**(1/2)

'''
Função que retorna o item mais frequente em uma lista.
'''
def most_common(lst):
    return max(set(lst), key = lst.count)
