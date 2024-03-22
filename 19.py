from decimal import *
num = Decimal(input())
maximum = max(num.as_tuple()[1])
minimum = min(num.as_tuple()[1])
print([maximum+minimum, maximum][len(num.as_tuple()[1]) == -num.as_tuple()[2]])

