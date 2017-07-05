from Neuronio import *

class Grade:
    def __init__(self, tam_grade, tam_entrada):
        self.tam_grade = tam_grade
        self.grade = self.grade_aleatoria(tam_grade, tam_entrada)

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
                j.print_pesos()
                print()
            print(20 * "-")

    #   pos = (i, j)
    def vizinhos(self, pos):
        vizinhos = []
        tam_grade = self.tam_grade

        if pos[0] + 1 in range(tam_grade[0]) and pos[1] in range(tam_grade[1]):
            vizinhos.append([pos[0] + 1, pos[1]])

        if pos[0] in range(tam_grade[0]) and pos[1] + 1 in range(tam_grade[1]):
            vizinhos.append([pos[0], pos[1] + 1])

        if pos[0] in range(tam_grade[0]) and pos[1] - 1 in range(tam_grade[1]):
            vizinhos.append([pos[0], pos[1] - 1])

        if pos[0] - 1 in range(tam_grade[0]) and pos[1] + 1 in range(tam_grade[1]):
            vizinhos.append([pos[0] - 1, pos[1] + 1])

        if pos[0] - 1 in range(tam_grade[0]) and pos[1] - 1 in range(tam_grade[1]):
            vizinhos.append([pos[0] - 1, pos[1] - 1])

        if pos[0] + 1 in range(tam_grade[0]) and pos[1] - 1 in range(tam_grade[1]):
            vizinhos.append([pos[0] + 1, pos[1] - 1])

        if pos[0] + 1 in range(tam_grade[0]) and pos[1] - 1 in range(tam_grade[1]):
            vizinhos.append([pos[0] + 1, pos[1] + 1])

        if pos[0] - 1 in range(tam_grade[0]) and pos[1] in range(tam_grade[1]):
            vizinhos.append([pos[0] - 1, pos[1]])

        return vizinhos

    def melhor_neuronio(self, entrada):
        tam_grade = self.tam_grade
        
        melhor = ((0, 0), self.grade[0][0].soma_pesos(entrada))
        for i in range(0, tam_grade[0]):
            for j in range(0, tam_grade[1]):
                sd = self.grade[i][j].soma_pesos(entrada)
                if sd < melhor[1]:
                    melhor = ((i, j), sd)
        return melhor
