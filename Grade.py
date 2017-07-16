from Neuronio import *
from utilitario import most_common
from math import e
import time

'''
Classe principal que contêm a grade de neurônios, faz o treino e reconhece digitos
'''
class Grade:
    '''
    Construtor
    Recebe como parâmetros, respectivamente
        - Tamanho da grade de neurônios
        - Tamanho do bloco de entrada
        - Taxa de aprendizado
        - Decrescimento da daxa de aprendizado (linear em cada iteração)
        - Sigma da função de vizinhança
        - Decrecimento do Sigma (linear em cada iteração)
    '''
    def __init__(self, tam_grade, tam_entrada, alpha, taxa, sigma, s_taxa):
        self.taxa = taxa
        self.sigma = sigma
        self.s_taxa = s_taxa
        self.alpha = alpha
        self.tam_grade = tam_grade
        self.tam_entrada = tam_entrada
        self.grade = self.grade_aleatoria(tam_grade, tam_entrada)
        self.BMU = None
        self.neighbors_size = 8
        self.rec_grid = None

    '''
    Função que reconhece um único dígito.
    Recebe como parâmetro o bloco de entrada (matriz) que representa um dígito e
    retorna o número reconhecido a partir dela. Para isso, encontra o BMU para a
    entrada e tenta pegar o valor no dicionário de reconhecimento do neurônio
    que reconheceu. Se não conseguir é um erro.
    '''
    def reconhece_digito(self, entrada):
        #   Encontra o BMU
        indice = self.reconhece2(entrada)[0]

        #   Tenta pegar o valor do número reconhecido
        try:
            d = self.rec_grid[indice]
        #   Se não conseguiu, é porque é um erro
        except:
            d = -1
        return d

    '''
    Função que faz o reconhecimento de uma lista de entradas. Faz a contagem de
    acertos e retorna a porcentagem dos mesmos. As entradas contem o número que
    representam (indice 1) para verificar se reconheceu corretamente.
    '''
    def reconhece_lista(self, lista_de_teste):
        hits = 0
        for i in lista_de_teste:
            #   i = [matriz, numero_que_a_matrix_representa]
            d = self.reconhece_digito(i[0])
            if d == i[1]:
                hits += 1
        #   Retorna a porcentagem de acertos
        return ((hits / len(lista_de_teste)) * 100)

    '''
    Função que gera a grade de reconhecimento. Recebe como parâmetro uma lista
    de entradas para gerar a grade. Faz o reconhecimento de toda a entrada e
    deixa como reconhecimento final de cada neurônio o numero que foi reconhecido
    com maior frequência.
    '''
    def grade_de_reconhecimento(self, lista_de_teste):
        desenhar = {}
        # Reconhece a entrada
        for i in lista_de_teste:
            z = self.reconhece2(i[0])
            try:
                desenhar[z[0]].append(i[1])
            except:
                desenhar[z[0]] = [i[1]]
        # Reconhece o mais frequente
        for i in desenhar:
            desenhar[i] = most_common(desenhar[i])

        self.rec_grid = desenhar

    '''
    Retorna o neurônio que reconhece a entrada, que é o BMU para a entrada.
    '''
    def reconhece2(self, entrada):
        #   Retorna o BMU para a entrada
        return self.melhor_neuronio(entrada)

    '''
    Função que faz o treinamento para uma lista de entradas.
    Chama a função iteração() para cada item da lista.
    '''
    def treinar(self, entrada_de_treino):
        alpha = self.alpha
        c = 0
        a = len(entrada_de_treino)
        for i in entrada_de_treino:
            print("%d/%d" %(c, a), end = "\r")
            self.iteracao(i, alpha)
            c += 1
        print("%d/%d" %(c, a))


    def repesa_neuronio(self, indice_neuronio, entrada, alpha):
        neuronio = self.grade[indice_neuronio[0]][indice_neuronio[1]]
        return neuronio.pesos + self.vizinhanca2(indice_neuronio) * alpha * (entrada - neuronio.pesos)

    '''
    Função que faz o treino para uma única entrada.
    Encontra o BMU e repesa toda a vizinhança. Neste caso, como a vizinhança é
    toda a grade de neurônios, o próprio BMU também é atualizado. Também é possível
    usar a vizinhança como os 8 neurônios ao redor do BMU, trocando a função vizinhos2()
    por vizinhos().
    '''
    def iteracao(self, entrada, alpha):
        #   Encontra o BMU
        self.BMU = self.melhor_neuronio(entrada)

        #   Repesa a vizinhança
        for i in self.vizinhos2(self.BMU[0]):
            self.grade[i[0]][i[1]].pesos = self.repesa_neuronio((i[0], i[1]), entrada, alpha)

    '''
    Função que retorna a lista de neurônios vizinhos do BMU, neste caso, a grade
    toda.
    '''
    def vizinhos2(self, x):
        l = [x]
        for i in range(self.tam_grade[0]):
            for j in range(self.tam_grade[1]):
                l.append((i, j))
        self.neighbors_size = len(l)
        return l

    '''
    Função de vizinhança (phi).
    Calcula a vizinhança utilizando o sigma como o tamanho da grade.
    Ver a função vizinhanca2() abaixo.
    '''
    def vizinhanca(self, indice_neuronio):
        neuronio = self.grade[indice_neuronio[0]][indice_neuronio[1]]
        melhor = self.grade[self.BMU[0][0]][self.BMU[0][1]]
        S = neuronio.soma_de_pesos(melhor.pesos)
        return e ** ((-(S ** 2)) / (2 * ((self.tam_entrada[0] * self.tam_entrada[1]) ** 2)))

    '''
    Função de vizinhança (phi).
    Calcula o valor de vizinhança utilizando o sigma da grade que é decrementado
    durante as iterações.
    '''
    def vizinhanca2(self, indice_neuronio):
        #   Calcula a distância euclidiana na grade entre o neuronio atual e o BMU
        melhor = self.grade[self.BMU[0][0]][self.BMU[0][1]]
        S = dist_eclidiana(indice_neuronio, self.BMU[0])

        #   Retorna o cálculo de vizinhança
        return e ** ((-(S ** 2)) / (2 * ((self.sigma) ** 2)))

    '''
    Função que gera a grade de neurônios inicial com pesos aleatórios.
    '''
    def grade_aleatoria(self, tam_grade, tam_entrada):
        grade = []
        for i in range(tam_grade[0]):
            linha = []
            for j in range(tam_grade[1]):
                linha.append(Neuronio(tam_entrada, True))
            grade.append(linha)
        return grade

    '''
    Função para imprimir a grade no terminal. Não está sendo usada já que está
    montando as imagens e as grades são muito grandes.
    '''
    def print_grade(self):
        for i in self.grade:
            for j in i:
                print(j.pesos)
                print()
            print(20 * "-")


    '''
    Função que encontra o BMU.
    Encontra a menor diferença da soma dos pesos (ditância euclidiana) entre a
    entrada e cada neurônio da grade.
    '''
    def melhor_neuronio(self, entrada):
        tam_grade = self.tam_grade
        melhor = ((0, 0), self.grade[0][0].soma_de_pesos(entrada))
        for i in range(0, tam_grade[0]):
            for j in range(0, tam_grade[1]):
                sd = self.grade[i][j].soma_de_pesos(entrada)
                if sd < melhor[1]:
                    melhor = ((i, j), sd)
        return melhor


    '''
    Função para pegar os 8 vizinhos de um neurônio. Recebe os indices da matriz
    e retorna a lista de vizinhos.
    '''
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
            vizinhos.append([pos[0] + 1, pos[1] - 1])

        if pos[0] - 1 in range(tam_grade[0]) and pos[1] in range(tam_grade[1]):
            vizinhos.append([pos[0] - 1, pos[1]])

        self.neighbors_size = len(vizinhos)
        return vizinhos
