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
test_list = input_grids[:30]

g = Grade((10, 10), (32, 32), 0.1, 0.00001)
carregar(g, "output/toda-entrada.tra.out")

print("> Iniciando treinamento")
ti = time.time()
g.treinar(test_list)
tf = time.time()
print("> Término do treinamento")

print()
print(">>> Tempo de treinamento: %fs"%(tf - ti))
print(">>> Tempo total:          %fs" %(tf - t0))
'''
'''

alpha = 50
m = 200
fs = 20
im = Image.new('RGB', (g.tam_grade[0] * m, g.tam_grade[1] * m), (200, 200, 200))
dr = ImageDraw.Draw(im, "RGBA")

for i in range(g.tam_grade[0]):
    for j in range(g.tam_grade[1]):
        dr.rectangle( ((i * m, j * m), (i * m + m, j * m + m)), fill=(255, 255, 255, 255), outline = "black")


'''
armazenar(g, "output/toda-entrada.tra.out")
'''

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
lista_de_treino = get_input_blocks_training("input/optdigits-orig.tra.in")[:100]
for i in lista_de_treino:
    z = g.reconhece(i[0])
    try:
        desenhar[z[0]].append(i[1])
    except:
        desenhar[z[0]] = [i[1]]
    print(z[0])


for i in desenhar:
    print(i, desenhar[i])



for i in desenhar:
    c = 0
    for j in desenhar[i]:
        dr.rectangle( ((i[1] * m, i[0] * m), (i[1] * m + m, i[0] * m + m)), fill = colors[j], outline = "black")
        dr.text(((i[1] * m) + c * fs * 2/3, i[0] * m + m/2 - fs/2), j, font=fnt, fill=(0, 0, 0))
        c += 1
'''
    #desenhar[i]

    dr.rectangle( ((z0[0][1] * m, z0[0][0] * m), (z0[0][1] * m + m, z0[0][0] * m + m)), fill = colors[i[1]], outline = "black")
    dr.text((z0[0][1] * m + m/2 - fs/2, z0[0][0] * m + m/2 - fs/2), i[1], font=fnt, fill=(255, 0, 0))
'''


im.save("teste.png")
