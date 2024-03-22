s = input()
res = {}
for i in s:
    res[i] = res.get(i, 0) + 1

pom = {}

for key, value in res.items():
    pom[str(value)] = key
for i in range(int(input())):
    value, key = input().split(sep=': ')
    res[pom[key]] = value
result = [res[i] for i in s]
print(''.join(result))