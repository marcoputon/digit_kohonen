import random
from utilitario import *
import numpy as np

class Neuronio:
    '''
    Construtor.
    Classe que guarda a grade de pesos.
    Pode iniciar os neurônios com pesos aleatórios entre 0 e 1 ou todos os pesos
    com valor 1.
    '''
    def __init__(self, tamanho, aleatorio):
        self.tamanho = tamanho
        if aleatorio == True:
            self.pesos = self.pesos_aleatorios(tamanho)
        else:#
            #   Gera a grade de pesos do neurônio com peso 1
            self.pesos = np.array(tamanho[0] * [tamanho[1] * [1]])


    '''
    Função que gera a grade de pesos do neurônio com pesos aleatórios.
    '''
    def pesos_aleatorios(self, tamanho):
        pesos = []
        for i in range(tamanho[0]):
            linha = []
            for j in range(tamanho[1]):
                linha.append(random.uniform(0, 1))
            pesos.append(linha)
        return np.array(pesos)


    '''
    Função para imprimir os pesos. Não está sendo usada.
    '''
    def print_pesos(self):
        for i in self.pesos:
            for j in i:
                print("%.2f" %j, end=" ")
            print()


    '''
    Função que calcula a distância (diferença) entre dois neurônios. faz a distancia
    soma da distância euclidiana de todos os índices.
    '''
    def soma_de_pesos(self, entrada):
        return sum(sum((entrada - self.pesos) ** 2))
