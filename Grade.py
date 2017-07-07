from Neuronio import *
from math import e

class Grade:
    def __init__(self, tam_grade, tam_entrada, alpha, taxa):
        self.taxa = taxa
        self.alpha = alpha
        self.tam_grade = tam_grade
        self.tam_entrada = tam_entrada
        self.grade = self.grade_aleatoria(tam_grade, tam_entrada)
        self.BMU = None

    def reconhece(self, entrada):
        self.iteracao(entrada, self.alpha)
        return self.BMU

    def treinar(self, entrada_de_treino):
        alpha = self.alpha
        c = 0
        a = len(entrada_de_treino)
        for i in entrada_de_treino:
            print("%d/%d" %(c, a), end = "\r")
            self.iteracao(i, alpha)
            alpha *= self.taxa
            c += 1
        print("%d/%d" %(c, a))


    def repesa_neuronio(self, neuronio, entrada, alpha):
        return neuronio.pesos + self.vizinhanca(neuronio) * alpha * (entrada - neuronio.pesos)


    def iteracao(self, entrada, alpha):
        self.BMU = self.melhor_neuronio(entrada)
        for i in range(self.tam_grade[0]):
            for j in range(self.tam_grade[1]):
                self.grade[i][j].pesos = self.repesa_neuronio(self.grade[i][j], entrada, alpha)

    def vizinhanca(self, neuronio):
        melhor = self.grade[self.BMU[0][0]][self.BMU[0][1]]
        S = neuronio.soma_de_pesos(melhor.pesos)
        return e ** ((-(S ** 2)) / (2 * ((self.tam_entrada[0] * self.tam_entrada[1]) ** 2)))


    def grade_aleatoria(self, tam_grade, tam_entrada):
        grade = []
        for i in range(tam_grade[0]):
            linha = []
            for j in range(tam_grade[1]):
                linha.append(Neuronio(tam_entrada, True))
            grade.append(linha)
        return grade


    def print_grade(self):
        for i in self.grade:
            for j in i:
                print(j.pesos)
                print()
            print(20 * "-")


    def melhor_neuronio(self, entrada):
        tam_grade = self.tam_grade
        melhor = ((0, 0), self.grade[0][0].soma_de_pesos(entrada))
        for i in range(0, tam_grade[0]):
            for j in range(0, tam_grade[1]):
                sd = self.grade[i][j].soma_de_pesos(entrada)
                if sd < melhor[1]:
                    melhor = ((i, j), sd)
        return melhor
