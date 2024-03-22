res = {}
for i in range(int(input())):
    key, value = input().split(sep=': ')
    res[key.lower()] = value
for i in range(int(input())):
    print(res.get(input().lower(), 'Не найдено'))