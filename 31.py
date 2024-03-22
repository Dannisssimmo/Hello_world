from functools import reduce


def pretty_print(data, side = '-', delimiter='|'):
    delimiter = ' ' + delimiter + ' '
    datas = reduce(lambda x, y: str(x)+delimiter+str(y), data)
    datas =delimiter[1:]+ datas + delimiter[:-1]
    sides = ' '+side*(len(datas)-2)+' '
    print(sides)
    print(datas)
    print(sides)



