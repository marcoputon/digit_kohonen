from Grade import *
from Leitura import *

def distancia(a, b):
    return ((a - b) ** 2) ** (1/2)

input_grids = get_input_blocks("input/optdigits-orig.tra.in")

g = Grade((3, 3), (3, 3))
