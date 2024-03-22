result = {}
for i in range(int(input())):
    name, t, count = input().split()
    count = int(count)
    result.setdefault(name, {})
    result[name][t] = result[name].get(t, 0) + count
for name in sorted(result):
    print(name + ':')
    for t, count in sorted(result[name].items()):
        print(t + ' ' + str(count))
