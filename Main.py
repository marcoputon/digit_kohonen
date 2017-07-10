import numpy as np
from Grade import *
from Leitura import *
from Saida import *
from PIL import Image, ImageFont, ImageDraw
import time
np.set_printoptions(threshold=np.inf)

t0 = time.time()
print("> Lendo arquivo de entrada")
input_grids = get_input_blocks("input/optdigits-orig.windep.in")
entrada_treino = get_input_blocks("input/optdigits-orig.tra.in")
test_list = entrada_treino[:100]

g = Grade((20, 20), (32, 32), 0.8, 0.7)
#carregar(g, "output/toda-entrada.tra.out")

for i in range(20):
    print("> Iniciando treinamento -", i)
    ti = time.time()
    g.treinar(entrada_treino)
    g.alpha *= g.taxa
    iteracao(g, i)
    tf = time.time()
    print("> Término do treinamento")

print()
print(">>> Tempo de treinamento: %fs"%(tf - ti))
print(">>> Tempo total:          %fs" %(tf - t0))
'''
'''
armazenar(g, "output/toda-entrada.tra.out")
