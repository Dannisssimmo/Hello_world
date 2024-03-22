n = int(input())
ar = [[input().split()[1] for j in range(int(input()))] for i in range(n)]
print(['NO', 'YES'][all(map(lambda x: '5' in x, ar))])
