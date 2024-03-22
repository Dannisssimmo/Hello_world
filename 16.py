import random
import string


def generate_index():
    res = []
    num = list(range(100))
    let = string.ascii_uppercase
    for i in range(6):
        if i == 2 or i == 3:
            res.append(str(random.choice(num)))
            if i == 2:
                res.append('_')
        else:
            res.append(random.choice(let))
    return ''.join(res)

print(generate_index())