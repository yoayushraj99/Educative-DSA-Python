# Return the first upper_case character

def find_first_upper(str, i=0):
    if str[i].isupper():
        return str[i]
    if i == len(str)-1:
        return "No upper case character found"
    return find_first_upper(str, i+1)


print(find_first_upper("heyBaby"))
