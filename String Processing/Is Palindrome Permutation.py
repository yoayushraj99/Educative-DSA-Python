def is_palin_perm(s):
    s = s.replace(" ", "").lower()

    count = dict()

    for i in s:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1

    if len(s) % 2 == 0:
        for i in count.keys():
            if count[i] % 2 != 0:
                return False
        return True
    else:
        odd_count = 0
        for i in count.keys():
            if count[i] % 2 != 0:
                if count[i] == 1:
                    odd_count += 1
                if odd_count > 1:
                    return False
        return True


palin_perm = "Tact Coa"
not_palin_perm = "This is not a palindrome permutation"

print(is_palin_perm(palin_perm))
print(is_palin_perm(not_palin_perm))
