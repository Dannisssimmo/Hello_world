nums = [-5, -4, 1, 2, 3]
res = [None] * len(nums)
x = 0
y = len(nums) - 1
for i in range(len(nums) - 1, -1, -1):
    if nums[x] ** 2 > nums[y] ** 2:
        res[i] = nums[x] ** 2
        x += 1
    else:
        res[i] = nums[y] ** 2
        y -= 1
print(res)
