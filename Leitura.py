def read_input(path):
    foo = open(path)

    f = []
    for i in foo:
        f.append(i[:len(i) - 1])
    return f[21:]

def split_block(f):
    blocks = []
    block = []
    for i in f:
        if len(i) == 2:
            blocks.append(block)
            block = []
        else:
            int_list = []
            for j in i:
                int_list.append(int(j))
            block.append(int_list)
    return blocks

def get_input_blocks(path):
    return split_block(read_input(path))
