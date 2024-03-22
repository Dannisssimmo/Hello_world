x = map(float, input().split())
y = map(float, input().split())
z = map(float, input().split())

xyz = list(zip(x, y, z))
print(all(map(lambda abc: abc[0] ** 2 + abc[1] ** 2 + abc[2] ** 2 <= 4, xyz)))
