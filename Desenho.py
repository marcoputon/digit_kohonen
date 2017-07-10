from PIL import Image, ImageFont, ImageDraw
from Grade import *

def desenha_grade(g):
    m = 50
    im = Image.new('RGB', (g.tam_grade[0] * m, g.tam_grade[1] * m), (200, 200, 200))
    dr = ImageDraw.Draw(im, "RGBA")

    for i in range(g.tam_grade[0]):
        for j in range(g.tam_grade[1]):
            dr.rectangle( ((i * m, j * m), (i * m + 50, j * m + 50)), fill='white', outline = "black")

    im.save("teste.png")
