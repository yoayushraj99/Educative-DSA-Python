def str_to_int(input_str):
    int = 0
    is_negative = False
    if input_str[0] == '-':
        is_negative = True
        input_str = input_str[1:]

    for idx, value in enumerate(input_str):
        digit = ord(value) - ord('0')
        int += digit*10**(len(input_str)-idx-1)

    if is_negative:
        int *= -1
    return int


print(str_to_int("-121"))
