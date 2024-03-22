default = {}
baza = {'write': 'W', 'read': 'R', 'execute': 'X'}
for i in range(int(input())):
    s = input().split()
    default[s[0]] = s[1:]
for i in range(int(input())):
    v, k = input().split()
    print(['Access denied', 'OK'][baza[v] in default[k]])
    # if s[k].lower() == v[0]:
    #     print('OK')
    # else:
    # print('Access denied')
