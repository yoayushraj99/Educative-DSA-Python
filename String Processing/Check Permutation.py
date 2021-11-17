def is_perm_1(str_1, str_2):
    str_1 = str_1.lower()
    str_2 = str_2.lower()

    if len(str_1) != len(str_2):
        return False

    d = dict()

    for i in str_1:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    for i in str_2:
        if i in d:
            d[i] -= 1
        else:
            return False

    for k, v in d.items():
        if v != 0:
            return False
    return True

is_permutation_1 = "google"
is_permutation_2 = "ooggle"

not_permutation_1 = "not"
not_permutation_2 = "top"

print(is_perm_1(is_permutation_1, is_permutation_2))
print(is_perm_1(not_permutation_1, not_permutation_2))
