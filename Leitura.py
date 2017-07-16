import numpy as np


'''
Leitura do arquivo de entrada ignorando as 20 primeiras linhas
'''
def read_input(path):
    foo = open(path)

    f = []
    for i in foo:
        f.append(i[:len(i) - 1])
    return f[21:]


'''
Quebra o arquivo de entrada em blocos e cria uma lista de matrizes que representam
números, ignorando o número que representam.
'''
def split_block(f):
    blocks = []
    block = []
    for i in f:
        if len(i) == 2:
            blocks.append(np.array(block))
            block = []
        else:
            int_list = []
            for j in i:
                int_list.append(int(j))
            block.append(int_list)
    return blocks


'''
Chamar essa função para ler as entradas que não precisam do numero que a matriz
representa
'''
def get_input_blocks(path):
    return split_block(read_input(path))


'''
Chamar essa função quando precisar do numero que a matriz representa.
'''
def get_input_blocks_training(path):
    return split_block_training(read_input(path))


'''
Quebra o arquivo de entrada em blocos e cria uma lista de matrizes que representam
números com o número que representam.
'''
def split_block_training(f):
    blocks = []
    block = []
    for i in f:
        if len(i) == 2:
            blocks.append([np.array(block), i[1:]])
            block = []
        else:
            int_list = []
            for j in i:
                int_list.append(int(j))
            block.append(int_list)
    return blocks
