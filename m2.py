def umn(a, b):
    result = [[0 for i in range(len(b[0]))] for i in range(len(a))]
    for i in range(len(result)):
        for j in range(len(result[0])):
            for l in range(len(a[0])):
                result[i][j] += a[i][l] * b[l][j]
    return result


n = int(input())
a = [[int(i) for i in input().split()] for i in range(n)]
x = int(input())
res = a.copy()
for i in range(x-1):
    res = umn(res, a)
for i in res:
    print(*i)

