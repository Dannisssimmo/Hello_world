data = {}
for i in range(int(input())):
    number, name = input().lower().split()
    data.setdefault(name, []).append(number)
for _ in range(int(input())):
    name = input().lower()
    # if name in data:
    #     print(*data[name])
    # else:
    #     print('абонент не найден')
    print(*data.get(name.lower(), ['абонент не найден']))