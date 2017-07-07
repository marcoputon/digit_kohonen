import numpy as np
from Grade import *
from Leitura import *
import time

t0 = time.time()
print("> Lendo arquivo de entrada")
input_grids = get_input_blocks("input/optdigits-orig.tra.in")
test_list = input_grids[:10]

g = Grade((5, 5), (32, 32), 1, 0.5)

print("> Iniciando treinamento")
ti = time.time()
g.treinar(input_grids)
tf = time.time()
print("> Término do treinamento")

print()
print(">>> Tempo de treinamento: %fs"%(tf - ti))
print(">>> Tempo total:          %fs" %(tf - t0))
