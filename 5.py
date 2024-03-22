n, m = (int(input()) for i in range(2))
s1 = set()
s2 = set()
for i in range(n + m):
    s = input()
    if s not in s1 and len(s1) < n:
        s1.add(s)
    else:
        s2.add(s)
print(len(s1^s2))
