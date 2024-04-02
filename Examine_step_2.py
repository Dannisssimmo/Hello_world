n, m = map(int, input().split())
start_opt = {}
for i in range(m):
    u, v, t = map(int, input().split())
    start_opt[(u, v)] = t

pred_opt = {}
k = int(input())
for i in range(k):
    u, v, t, c = map(int, input().split())
    pred_opt.setdefault((u, v), []).append([c, t, i])

p = int(input())
result = []
for i in range(p):
    u, v, t = map(int, input().split())
    if start_opt.setdefault((u,v), 1000000000) > t and result != -1:
        if pred_opt.setdefault((u, v), []):
            sorted_uv = sorted(pred_opt[(u, v)])
            for j in sorted_uv:
                if j[1] < t:
                    result.append(j[2])
                elif j == sorted_uv[-1]:
                    result = -1

if result == -1:
    print(-1)
elif result:
    print(*sorted(result))
else:
    print(0)

