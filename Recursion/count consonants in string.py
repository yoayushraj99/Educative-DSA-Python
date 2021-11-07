def count_consonant(s):
    vowels = "aeiou"
    if not s:
        return 0
    if s[0].lower() not in vowels and s[0].isalpha():
        return count_consonant(s[1:])+1
    else:
        return count_consonant(s[1:])


print(count_consonant("abcdefghi"))
