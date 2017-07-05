import random

class Neuronio:
    def __init__(self, tamanho, aleatorio):
        if aleatorio == True:
            self.pesos = self.pesos_aleatorios(tamanho)
        else:
            self.pesos = tamanho[0] * [tamanho[1] * [1]]

    def pesos_aleatorios(self, tamanho):
        pesos = []
        for i in range(tamanho[0]):
            linha = []
            for j in range(tamanho[1]):
                linha.append(random.uniform(0, 1))
            pesos.append(linha)
        return pesos

    def print_pesos(self):
        for i in self.pesos:
            for j in i:
                print("%.2f" %j, end=" ")
            print()
