import string

s = input()
ind = any(map(lambda x: x in string.digits, s))
inS = any(map(lambda x: x in string.ascii_uppercase, s))
ins = any(map(lambda x: x in string.ascii_lowercase, s))

print(['NO', 'YES'][all([ind, ins, inS]) and len(s) >= 7])
