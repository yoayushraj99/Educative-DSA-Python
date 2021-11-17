def int_to_str(input_int):
    string = ""
    x = ""
    if input_int < 0:
        string += "-"
        input_int *= -1
    elif input_int == 0:
        return chr(ord('0'))
    while input_int > 0:
        last_digit = input_int % 10
        x += chr(ord('0') + last_digit)
        input_int = input_int // 10

    x = x[::-1]
    string += x

    return string, type(string)


print(int_to_str(0))
