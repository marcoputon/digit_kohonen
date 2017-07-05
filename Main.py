import numpy as np
from Grade import *
from Leitura import *

input_grids = get_input_blocks("input/optdigits-orig.tra.in")

g = Grade((3, 3), (2, 2))

g.print_grade()

print(g.grade[0][0].soma_pesos([[1, 1], [1, 1]]))
