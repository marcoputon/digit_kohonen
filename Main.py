from PIL import Image, ImageFont, ImageDraw
import numpy as np
import time
from Grade import *
from Leitura import *
from Saida import *
from Desenho import *

########################## VARIAVEIS DE CONFIGURAÇÂO ##########################

carregar_treino = "output/0.5-0.85toda-entrada.tra.out" # Arquivo de treino armazenado anteriormente
treinar         = "input/optdigits-orig.tra.in"         # Arquivo de entrada para treinar
teste_de_acerto = "input/optdigits-orig.windep.in"      # Arquivo de entrada para testar taxa de acerto
teste_de_treino = "input/optdigits-orig.cv.in"          # Arquivo de entrada gerar a grade de reconhecimento
n_iter          = 5                                     # Quantidade de iterações de treino

CARREGAR_TREINO                 = True
TREINAR                         = False
ARMAZENAR                       = False
GERAR_GRADE_RECONHECIMENTO      = True
CALCULAR_TAXA_ACERTOS           = True
DESENHAR_GRADE_MESCLADA         = False
DESENHAR_GRADE_RECONHECIMENTO   = False

###############################################################################

t0 = time.time()
print("> Lendo arquivo de entrada")
entrada_acertos = get_input_blocks_training(teste_de_acerto)
entrada_treino = get_input_blocks(treinar)
entrada_teste = get_input_blocks_training(teste_de_treino)

print("> Gerando grade de neurônios")
g = Grade((20, 20), (32, 32), 0.5, 0.85)

if CARREGAR_TREINO:
    print("> Carregando treino")
    carregar(g, carregar_treino)

if TREINAR:
    print("> Treinando")
    ti = time.time()
    for i in range(n_iter):
        print("> Treinamento -", i)
        g.treinar(entrada_treino)
        g.alpha *= g.taxa
    tf = time.time()
    print()
    print(">>> Tempo de treinamento: %fs"%(tf - ti))

if ARMAZENAR:
    print("> Armazenando treino")
    armazenar(g, "output/toda-entrada.tra.out")

if GERAR_GRADE_RECONHECIMENTO:
    print("> Gerando grade de reconhecimento")
    g.grade_de_reconhecimento(entrada_teste)

if CALCULAR_TAXA_ACERTOS:
    print("> Calculando taxa de acertos")
    taxa_de_acerto = g.reconhece_lista(entrada_acertos)
    print("  - Taxa de acerto: %.4f" %(taxa_de_acerto))

if DESENHAR_GRADE_MESCLADA:
    print("> Desenhando grade mesclada")
    desenha_grade(g, True, "input/optdigits-orig.cv.in", "output/images/grade_mesclada.png")    #   IMAGEM MESCLADA

if DESENHAR_GRADE_RECONHECIMENTO:
    print("> Desenhando grade de reconhecimento")
    desenha_grade(g, False, "input/optdigits-orig.cv.in", "output/images/grade_final.png")      #   IMAGEM FINAL

print("# Tempo total: %fs" %(time.time() - t0))
