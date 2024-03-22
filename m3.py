n, m = map(int, input().split())
for i in range(n):
    row = []
    for j in range(m):
        if i%2==0:
            if j%2 == 0:
                row.append('.')
            else:
                row.append('*')
        else:
            if j%2 == 0:
                row.append('*')
            else:
                row.append('.')
    print(*row, sep=' ')

