def is_match(x1, x2):
    if x1 == '(' and x2 == ')':
        return True
    elif x1 == '[' and x2 == ']':
        return True
    elif x1 == '{' and x2 == '}':
        return True
    else:
        return False


def is_paren_balanced(n: str) -> bool:
    stack = []

    for i in n:
        if i in '([{':
            stack.append(i)
        else:
            if not stack:
                return False
            else:
                top = stack.pop()
                if not is_match(top, i):
                    return False

    return stack == []


print(is_paren_balanced('({})[]'))
