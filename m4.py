n, m = map(int, input().split())
arr = [[0 for i in range(m)] for i in range(n)]
count = 1
for j in range(m):
    for i in range(n):
        arr[i][j] = count
        count += 1
for i in arr:
    print(*i)
