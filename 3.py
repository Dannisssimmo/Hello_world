def comma(num):
    work_with = list(str(num))
    while work_with:
        if work_with == list(str(num)):
            result = work_with[-4:-1]
        else:
            result = work_with[-4:-1] + [','] + result
        print(work_with)
        work_with = work_with[0:len(work_with)-3]
    print(work_with)
    return ''.join(result)


print(comma(1234567890))
