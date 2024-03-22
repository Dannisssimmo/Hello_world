n = int(input())
for k in [[abs(i - j) for i in range(n)] for j in range(n)]:
    print(*k, sep=' ')


# [print(*[abs(i - j) for i in range(n)]) for j in range(n)]
