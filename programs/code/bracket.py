def matched(s):
    stack = []

    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if len(stack) == 0 or stack[-1] != '(':
                return False
            stack.pop()
    return len(stack) == 0


print(matched("zb%78"))
print(matched("(7)(a"))
