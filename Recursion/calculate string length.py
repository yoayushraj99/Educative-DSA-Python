# return the length of input_string

def str_len(s):
    if not s:
        return 0
    return str_len(s[1:]) + 1


print(str_len("abc"))
