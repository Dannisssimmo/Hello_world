def mean(*args):
    tr = (int, float)
    ar = [i for i in args if type(i) in tr]
    if len(ar) != 0:
        res = sum(ar)/len(ar)
    else:
        res = 0
    return res

print(mean())
print(mean(7))
print(mean(1.5, True, ['stepik'], 'beegeek', 2.5, (1, 2)))
print(mean(True, ['stepik'], 'beegeek', (1, 2)))
print(mean(-1, 2, 3, 10, ('5')))
print(mean(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))