n = int(input())
ar = [input() for i in range(n)]


def ipCoun(IP):
    x1, x2, x3, x4 = map(int, IP.split('.'))
    return x1 * 256 ** 3 + x2 * 256 ** 2 + x3 * 256 + x4


print(*sorted(ar, key=ipCoun), sep='\n')
