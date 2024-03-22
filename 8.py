n = int(input())
res = {}
for i in range(n):
    inp = input().split()
    for _ in inp[1:]:
        res[_] = inp[0]
n = int(input())
for i in range(n):
    print(res[input()])
