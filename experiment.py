from time import time

st = '1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 ' \
     '7 8 9 0'
rez1 = 0
rez2 = 0
time_start_1 = time()
for i in range(10000):
    str1 = [int(i) for i in st.split(' ')]
time_stop_1 = time()
print(time_stop_1 - time_start_1)

time_start_2 = time()
for i in range(10000):
    str2 = list(map(int, st.split(' ')))
time_stop_2 = time()
print(time_stop_2 - time_start_2)
