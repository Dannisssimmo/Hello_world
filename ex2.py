matrix = [['.' for i in range(8)] for _ in range(8)]
place = list(input())

match = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
for i in range(len(match)):
    if place[0] == match[i]:
        place[0] = i
place[1] = 8 - int(place[1])
place[0], place[1] = place[1], place[0]
for i in range(8):
    for j in range(8):
        if i == place[0] or j == place[1] or abs(place[0]-i) == abs(place[1]-j):
            matrix[i][j] = '*'
matrix[place[0]][place[1]] = 'Q'
for i in matrix:
    print(*i, sep=' ')
