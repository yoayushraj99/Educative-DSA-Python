# 1, 11, 21, 1211, 111221, 312211, 13112221, ...

def next_number(s):
    arr = []
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i+1]:
            i += 1
            count += 1
        arr.append(str(count) + s[i])
        i += 1
    return ''.join(arr)


print(next_number('111222333'))
