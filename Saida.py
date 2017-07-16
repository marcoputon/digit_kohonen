import numpy as np
from Grade import *
from Leitura import *
import time


'''
Função para armazenar o treino.
Percorre toda a matriz de neurônios e escreve os valores no mesmo formato dos
arquivos de entrada.
'''
def armazenar(grade, path):
    f = open(path, "w")
    for i in range(21):
        f.write("perdi\n")

    for i in range(grade.tam_grade[0]):
        for j in range(grade.tam_grade[1]):
            ng = neuronio_para_string(grade.grade[i][j])
            for k in ng:
                f.write(k + "\n")
            f.write(" -\n")
    f.close()


'''
Gera a string com os pesos de um neurônio, para guardar o treino.
'''
def neuronio_para_string(neuronio):
    n = []
    for i in range(neuronio.tamanho[0]):
        l = ""
        for j in range(neuronio.tamanho[1]):
            l += str(neuronio.pesos[i, j]) + " "
            n.append(l[:len(l) - 1])
            return n


'''
##################################################################################
Funções iguais as do arquivo Leitura.py, com a diferença de que já cria os objetos
e colocam na grade que recebem como parametro.
##################################################################################
'''

def read_output(path):
    foo = open(path)

    f = []
    for i in foo:
        f.append(i[:len(i) - 1])
    return f[21:]


def split_block_out(f):
    blocks = []
    block = []
    for i in f:
        if len(i) == 2:
            blocks.append(np.array(block))
            block = []
        else:
            int_list = []
            m = i.split(" ")
            for j in m:

                int_list.append(float(j))
            block.append(int_list)
    return blocks




def get_output_blocks(path):
    return split_block_out(read_output(path))


def carregar(g, path):
    pesos = get_output_blocks(path)

    for i in range(g.tam_grade[0]):
        for j in range(g.tam_grade[1]):
            n = Neuronio(g.tam_entrada, False)
            n.pesos = pesos[i * g.tam_grade[0] + j]
            g.grade[i][j] = n
