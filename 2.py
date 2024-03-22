arr = [1,5,2,0,0,0,0,0,0]
i = 0
while i < len(arr):
    if arr[i] == 0 and i<len(arr):
        for j in range(len(arr) - 1, i, -1):
            arr[j] = arr[j-1]
        arr[i + 1] = 0
        i += 2
    else:
        i += 1
print(arr)
