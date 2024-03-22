n = int(input())
ar = [[int(i) for i in input().split()] for i in range(n)]
et = list(range(1, n + 1))
flag = True
for i in ar:
    if sorted(i) == et and flag:
        res = 'YES'
    else:
        flag = False
        res = 'NO'
for i in range(n):
    new_list = sorted([ar[j][i] for j in range(n)])
    if new_list==et and flag:
        res = 'YES'
    else:
        flag = False
        res = 'NO'
print(res)