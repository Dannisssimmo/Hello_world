a = input()
b = input()
com_index = []
commands = []

for i in range(len(b)):
    if b[i] == '<':
        com_index.append(i)
    if b[i] == '>':
        com_index.append(i + 1)

for i in range(1, len(com_index), 2):
    commands.append(''.join(b[com_index[i - 1]:com_index[i]]))
for i in commands:
    b = b.replace(i, '/')
result = []
curs = 0
for i in range(len(b)):
    if b[i] == '/':
        command = commands.pop(0)
        if command == '<left>' and curs != 0:
            curs -= 1
        elif command == '<right>' and curs != len(result):
            curs += 1
        elif command == '<delete>' and curs != len(result):
            del result[curs]
        elif command == '<bspace>' and curs != 0:
            del result[curs-1]
            curs -= 1
    else:
        result.insert(curs, b[i])
        curs += 1
result = ''.join(result)
print(['YES', 'NO'][result != a])
