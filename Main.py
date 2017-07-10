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
test_list = input_grids[:3]

g = Grade((10, 10), (32, 32), 0.1, 0.00001)
'''
carregar(g, "output/toda-entrada.tra.out")
'''

print("> Iniciando treinamento")
ti = time.time()
g.treinar(test_list)
tf = time.time()
print("> Término do treinamento")

print()
print(">>> Tempo de treinamento: %fs"%(tf - ti))
print(">>> Tempo total:          %fs" %(tf - t0))

alpha = 50
m = 50
im = Image.new('RGB', (g.tam_grade[0] * m, g.tam_grade[1] * m), (200, 200, 200))
dr = ImageDraw.Draw(im, "RGBA")

for i in range(g.tam_grade[0]):
    for j in range(g.tam_grade[1]):
        dr.rectangle( ((i * m, j * m), (i * m + 50, j * m + 50)), fill=(255, 255, 255, 255), outline = "black")


list0 = [input_grids[0], input_grids[10], input_grids[20]]
list1 = [input_grids[1], input_grids[11], input_grids[21]]
list2 = [input_grids[2], input_grids[12], input_grids[22]]
list3 = [input_grids[3], input_grids[13], input_grids[23]]
list4 = [input_grids[4], input_grids[14], input_grids[24]]
list5 = [input_grids[5], input_grids[15], input_grids[25]]
list6 = [input_grids[6], input_grids[16], input_grids[26]]
list7 = [input_grids[7], input_grids[17], input_grids[27]]
list8 = [input_grids[8], input_grids[18], input_grids[28]]
list9 = [input_grids[9], input_grids[19], input_grids[29]]

print("-- 0 --")
cor = (255, 0, 0, alpha)
z0 = g.reconhece(list0[0])
print(z0[0])
dr.rectangle( ((z0[0][1] * m, z0[0][0] * m), (z0[0][1] * m + 50, z0[0][0] * m + 50)), fill = cor, outline = "black")

z0 = g.reconhece(list0[1])
print(z0[0])
dr.rectangle( ((z0[0][1] * m, z0[0][0] * m), (z0[0][1] * m + 50, z0[0][0] * m + 50)), fill = cor, outline = "black")

z0 = g.reconhece(list0[2])
print(z0[0])
dr.rectangle( ((z0[0][1] * m, z0[0][0] * m), (z0[0][1] * m + 50, z0[0][0] * m + 50)), fill = cor, outline = "black")


print("-- 1 --")
cor = (0, 0, 255, alpha)
z0 = g.reconhece(list1[0])
print(z0[0])
dr.rectangle( ((z0[0][1] * m, z0[0][0] * m), (z0[0][1] * m + 50, z0[0][0] * m + 50)), fill = cor, outline = "black")

z0 = g.reconhece(list1[1])
print(z0[0])
dr.rectangle( ((z0[0][1] * m, z0[0][0] * m), (z0[0][1] * m + 50, z0[0][0] * m + 50)), fill = cor, outline = "black")

z0 = g.reconhece(list1[2])
print(z0[0])
dr.rectangle( ((z0[0][1] * m, z0[0][0] * m), (z0[0][1] * m + 50, z0[0][0] * m + 50)), fill = cor, outline = "black")

'''
print("-- 1 --")
print(g.reconhece(list1[0]))
print(g.reconhece(list1[1]))
print(g.reconhece(list1[2]))

print("-- 2 --")
print(g.reconhece(list2[0]))
print(g.reconhece(list2[1]))
print(g.reconhece(list2[2]))

print("-- 3 --")
print(g.reconhece(list3[0]))
print(g.reconhece(list3[1]))
print(g.reconhece(list3[2]))

print("-- 4 --")
print(g.reconhece(list4[0]))
print(g.reconhece(list4[1]))
print(g.reconhece(list4[2]))

print("-- 5 --")
print(g.reconhece(list5[0]))
print(g.reconhece(list5[1]))
print(g.reconhece(list5[2]))

print("-- 6 --")
print(g.reconhece(list6[0]))
print(g.reconhece(list6[1]))
print(g.reconhece(list6[2]))

print("-- 7 --")
print(g.reconhece(list7[0]))
print(g.reconhece(list7[1]))
print(g.reconhece(list7[2]))

print("-- 8 --")
print(g.reconhece(list8[0]))
print(g.reconhece(list8[1]))
print(g.reconhece(list8[2]))

print("-- 9 --")
print(g.reconhece(list9[0]))
print(g.reconhece(list9[1]))
print(g.reconhece(list9[2]))


armazenar(g, "output/toda-entrada.tra.out")
'''
im.save("teste.png")
