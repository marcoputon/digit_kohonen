from PIL import Image, ImageFont, ImageDraw
import time
from Leitura import *

def desenha_grade(g, mesclar, tra_path, save_path):
    ######   Parêmetros de desenho da grade   ######
    alpha = 50  #   canal alpha
    m = 200     #   Tamanho dos quadrados
    fs = 20     #   Tamanho da fonte

    im = Image.new('RGB', (g.tam_grade[0] * m, g.tam_grade[1] * m), (200, 200, 200))
    dr = ImageDraw.Draw(im, "RGBA")

    #   desenha a grade branca
    for i in range(g.tam_grade[0]):
        for j in range(g.tam_grade[1]):
            dr.rectangle( ((i * m, j * m), (i * m + m, j * m + m)), fill=(255, 255, 255, 255), outline = "black")

    #   Reconhece para desenhar a cor do número reconhecido
    desenhar = {}
    lista_de_teste = get_input_blocks_training(tra_path)

    tti = time.time()

    #   Se for gerar a grade mesclada, possui camada alpha
    if mesclar:
        for i in lista_de_teste:
            z = g.reconhece2(i[0])
            try:
                desenhar[z[0]].append(i[1])
            except:
                desenhar[z[0]] = [i[1]]
    #   Se não for gerar a grade mesclada, desenha a grade de reconhecimento.
    else:
        alpha = 255
        desenhar = g.rec_grid
    ttf = time.time()

    print("Tempo de reconhecimento: %fs" %(ttf - tti))

    #Fonte usada no ubuntu
    #fnt = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', fs)

    #fonte usada no arch linux
    fnt = ImageFont.truetype('/usr/share/texmf-dist/fonts/truetype/public/opensans/OpenSans-Bold.ttf', fs)


    #   Definição das cores de cada número.
    colors = {  '0':(255, 255, 0, alpha), #amarelo
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


    #   Primeiro desenhas os quadrados
    for i in desenhar:
        for j in desenhar[i]:
            dr.rectangle( ((i[1] * m, i[0] * m), (i[1] * m + m, i[0] * m + m)), fill = colors[j], outline = "black")

    #   Depois desenha os números que reconhece
    for i in desenhar:
        c = 0
        d = 1
        for j in desenhar[i]:
            dr.text(((i[1] * m) + c * fs * 2/3, i[0] * m + d*3/2 * fs/2), j, font = fnt, fill=(0, 0, 0))
            c += 1
            if (i[1] * m) + c * fs * 2/3 + fs > (i[1] * m) + m:
                c = 0
                d += 1


    im.save(save_path)
