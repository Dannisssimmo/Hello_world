import string

name = input()
set_name = set(name)
numbers = set('1234567890')
let_up = set(string.ascii_uppercase)
let_low = set(string.ascii_lowercase)
if len(name) >= 8 and (set_name & numbers) and set_name & let_up and set_name & let_low:
    print('YES')
else:
    print('NO')