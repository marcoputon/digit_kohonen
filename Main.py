import numpy as np
from Grade import *
from Leitura import *
from Saida import *
import time
np.set_printoptions(threshold=np.inf)

t0 = time.time()
print("> Lendo arquivo de entrada")
input_grids = get_input_blocks("input/optdigits-orig.tra.in")
test_list = input_grids[:100]

g = Grade((10, 10), (32, 32), 0.1, 0.01)

print("> Iniciando treinamento")
ti = time.time()
g.treinar(test_list)
tf = time.time()
print("> Término do treinamento")

print()
print(">>> Tempo de treinamento: %fs"%(tf - ti))
print(">>> Tempo total:          %fs" %(tf - t0))
'''
armazenar(g, "output/toda-entrada.tra.out")
carregar("output/toda-entrada.tra.out")
'''


list0 = [test_list[0], test_list[1], test_list[8]]
list7 = [test_list[2], test_list[10], test_list[17]]
list4 = [test_list[3], test_list[16], test_list[19]]

print("-- 0 --")
print(g.reconhece(list0[0]))
print(g.reconhece(list0[1]))
print(g.reconhece(list0[2]))

print("\n-- 7 --")
print(g.reconhece(list7[0]))
print(g.reconhece(list7[1]))
print(g.reconhece(list7[2]))

print("\n-- 4 --")
print(g.reconhece(list4[0]))
print(g.reconhece(list4[1]))
print(g.reconhece(list4[2]))
