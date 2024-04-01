with open('input.txt', 'r') as f:
    a, b = map(int, f.readline().split())
res = a + b
fi = open('output.txt', 'w')
fi.write(str(res))
fi.close()
