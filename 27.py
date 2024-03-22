x = int(input())
y = int(input())
# flag = True
# for i in range(x, y + 1):
#     flag = True
#     for j in str(i):
#         if j == "0":
#             flag = False
#         elif not (i % int(j) == 0 and flag):
#             flag = False
#     if flag:
#         print(i, end=' ')

for i in range(x, y + 1):
    digits = tuple(map(int, str(i)))

    if 0 not in digits and all((map(lambda curr_num: i % curr_num == 0, digits))):
        print(i, end=' ')
