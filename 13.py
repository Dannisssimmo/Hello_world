def merge(values):
    result = {}
    for i in values:
        for k, v in i.items():
            result.setdefault(k, set()).add(v)
    return result


result = merge([{'a': 1, 'b': 2}, {'b': 10, 'c': 100}, {'a': 1, 'b': 17, 'c': 50}, {'a': 5, 'd': 777}])
print(result)