import random

n = 10 ** 8  # количество испытаний
k = 0
for i in range(n):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2+y**2 <=1:
        k += 1
s = (k / n)*4
print(s)
