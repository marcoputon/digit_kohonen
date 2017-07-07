import random
from utilitario import *
import numpy as np

class Neuronio:
    def __init__(self, tamanho, aleatorio):
        self.tamanho = tamanho
        if aleatorio == True:
            self.pesos = self.pesos_aleatorios(tamanho)
        else:
            self.pesos = np.matrix(tamanho[0] * [tamanho[1] * [1]])

    def pesos_aleatorios(self, tamanho):
        pesos = []
        for i in range(tamanho[0]):
            linha = []
            for j in range(tamanho[1]):
                linha.append(random.uniform(0, 1))
            pesos.append(linha)
        return np.matrix(pesos)

    def print_pesos(self):
        for i in self.pesos:
            for j in i:
                print("%.2f" %j, end=" ")
            print()

    def soma_de_pesos(self, entrada):
        soma = 0
        for i in range(self.tamanho[0]):
            for j in range(self.tamanho[1]):
                soma += distancia(entrada[i, j], self.pesos[i, j])
        return soma

    def atualiza_peso(self, entrada, melhor):
        pass
