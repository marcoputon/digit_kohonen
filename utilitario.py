import numpy as np
from Grade import *
from Leitura import *
from Saida import *
from PIL import Image, ImageFont, ImageDraw
import time
np.set_printoptions(threshold=np.inf)

def iteracao(g, iter_number):
    alpha = 50
    m = 200
    fs = 20
    im = Image.new('RGB', (g.tam_grade[0] * m, g.tam_grade[1] * m), (200, 200, 200))
    dr = ImageDraw.Draw(im, "RGBA")

    for i in range(g.tam_grade[0]):
        for j in range(g.tam_grade[1]):
            dr.rectangle( ((i * m, j * m), (i * m + m, j * m + m)), fill=(255, 255, 255, 255), outline = "black")

    fnt = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', fs)
    colors = {'0':(255, 255, 0, alpha), #amarelo
              '1':(255, 128, 0, alpha), #laranja
              '2':(0, 255, 255, alpha), #azul_piscina
              '3':(0, 0, 255, alpha),   #azul
              '4':(255, 0, 255, alpha), #rosa
              '5':(0, 128, 255, alpha), #azul_twiter
              '6':(127, 0, 255, alpha), #roxo
              '7':(128, 255, 0, alpha), #verde_claro
              '8':(0, 255, 0, alpha),   #verde
              '9':(255, 0, 0, alpha)    #vermelho
    }

    desenhar = {}
    lista_de_treino = get_input_blocks_training("input/optdigits-orig.cv.in")
    tti = time.time()
    count = 0
    for i in lista_de_treino:
        print("%d" %(count), end = "\r")
        count += 1
        z = g.reconhece2(i[0])
        try:
            desenhar[z[0]].append(i[1])
        except:
            desenhar[z[0]] = [i[1]]
    ttf = time.time()

    for i in desenhar:
        for j in desenhar[i]:
            dr.rectangle( ((i[1] * m, i[0] * m), (i[1] * m + m, i[0] * m + m)), fill = colors[j], outline = "black")

    for i in desenhar:
        c = 0
        d = 1
        for j in desenhar[i]:
            dr.text(((i[1] * m) + c * fs * 2/3, i[0] * m + d*3/2 * fs/2), j, font = fnt, fill=(0, 0, 0))
            c += 1
            if (i[1] * m) + c * fs * 2/3 + fs > (i[1] * m) + m:
                c = 0
                d += 1

    im.save("output/imagens/iteracao" + str(iter_number) + ".png")


def distancia(a, b):
    return a - b

def dist_eclidiana(a, b):
    return ((a[0] - b[0])**2 + (a[1] - b[1])**2)**(1/2)


def som_matriz(a, b):
    r = []
    for i in range(len(a)):
        linha = []
        for j in range(len(a[0])):
            linha.append(a[i][j] + b[i][j])
        r.append(linha)
    return r

def sub_matriz(a, b):
    r = []
    for i in range(len(a)):
        linha = []
        for j in range(len(a[0])):
            linha.append(a[i][j] - b[i][j])
        r.append(linha)
    return r
