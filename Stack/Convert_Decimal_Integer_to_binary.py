def dec_to_bin(n: int, binary=''):
    if n == 0 or n == 1:
        return (binary + str(n))[::-1]
    binary += str(n % 2)
    n = n >> 1
    return dec_to_bin(n, binary)


print(dec_to_bin(100))
