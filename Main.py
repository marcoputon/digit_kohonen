from PIL import Image, ImageFont, ImageDraw
import numpy as np
import time
from Grade import *
from Leitura import *
from Saida import *
from Desenho import *

########################## VARIAVEIS DE CONFIGURAÇÂO ##########################

carregar_treino = "output/toda-entrada.tra.out"         # Arquivo de treino armazenado anteriormente
treinar         = "input/optdigits-orig.tra.in"         # Arquivo de entrada para treinar
teste_de_acerto = "input/optdigits-orig.tra.in"          # Arquivo de entrada para testar taxa de acerto
teste_de_treino = "input/optdigits-orig.cv.in"          # Arquivo de entrada gerar a grade de reconhecimento
n_iter          = 5                                     # Quantidade de iterações de treino

CARREGAR_TREINO                 = False
TREINAR                         = True
ARMAZENAR                       = False
GERAR_GRADE_RECONHECIMENTO      = True
CALCULAR_TAXA_ACERTOS           = True
DESENHAR_GRADE_MESCLADA         = True
DESENHAR_GRADE_RECONHECIMENTO   = True
GERAR_LOG_RESULTADO             = True

GRID_SIZE_I                     = 8
GRID_SIZE_J                     = 8

ALPHA_INICIAL                   = 0.1
DECRE_ALPHA                     = 0.00009

SIGMA_INICIAL                   = 2
DECRE_SIGMA                     = 0.0015
###############################################################################

t0 = time.time()
print("> Lendo arquivo de entrada")
entrada_acertos = get_input_blocks_training(teste_de_acerto)
entrada_treino = get_input_blocks(treinar)
entrada_teste = get_input_blocks_training(teste_de_treino)

print("> Gerando grade de neurônios")
g = Grade((GRID_SIZE_I, GRID_SIZE_J), (32, 32), ALPHA_INICIAL, DECRE_ALPHA, SIGMA_INICIAL, DECRE_SIGMA)
#def __init__(self, tam_grade, tam_entrada, alpha, taxa, sigma, s_taxa):


if CARREGAR_TREINO:
    print("> Carregando treino")
    carregar(g, carregar_treino)

if TREINAR:
    print("> Treinando")
    ti = time.time()
    for i in range(n_iter):
        print("> Época: ", i, "| alpha: %.6f"% g.alpha, "| sigma: %.6f"% g.sigma)
        g.treinar(entrada_treino)
        g.alpha -= g.taxa
        g.sigma -= g.s_taxa
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

if GERAR_LOG_RESULTADO:
    print("> Gerando arquivo com Log dos resultados")
    logFile = open('output/images/logResultados.txt', 'w')
    strtowrite = 'Parametros de entrada:\n'
    strtowrite += 'Tamanho da grade: ' + str(GRID_SIZE_I) + 'x' + str(GRID_SIZE_J) + '\n'
    strtowrite += 'Quantidade de épocas treinadas: ' + str(n_iter) +'\n'
    strtowrite += 'Alpha inicial: ' + str(ALPHA_INICIAL) +'\n'
    strtowrite += 'Sigma inicial: ' + str(SIGMA_INICIAL) +'\n'
    strtowrite += 'Decrementação alpha: ' + str(DECRE_ALPHA) +'\n'
    strtowrite += 'Decrementação Sigma: ' + str(DECRE_SIGMA) +'\n'
    
    strtowrite += '\n\nResultados:\n'
    strtowrite += 'taxa de acerto: ' + str(taxa_de_acerto) + '\n'
    
    logFile.write(strtowrite)
    logFile.close()

print("# Tempo total: %fs" %(time.time() - t0))