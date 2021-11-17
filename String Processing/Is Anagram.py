def is_anagram(s1, s2):
    dict = {}

    if len(s1) != len(s2):
        return False

    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    for i in s1:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1

    for i in s2:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] -= 1

    for i in dict.keys():
        if dict[i] != 0:
            return False
    return True


print(is_anagram("fairy tales", "rail safety"))


