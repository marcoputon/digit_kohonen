import numpy as np
from Grade import *
from Leitura import *
import time

def armazenar(grade, path):
    f = open(path, "w")

    for i in range(grade.tam_grade[0]):
        for j in range(grade.tam_grade[1]):
            ng = neuronio_para_string(grade.grade[i][j])
            for k in ng:
                f.write(k + "\n")
            f.write("-\n")
    f.close()


def neuronio_para_string(neuronio):
    n = []
    for i in range(neuronio.tamanho[0]):
        l = ""
        for j in range(neuronio.tamanho[1]):
            l += str(neuronio.pesos[i, j]) + " "
        n.append(l)
    return n

def carregar(path):
    foo = open(path)
    f = ""
    for i in foo:
        f += i

    f = f.split("-\n")

    for i in f:
        block = i.split(" ")
        print(block)
        print("------------------------------------------------")
