def braces(values):
    result = []
    for s in values:
        result.append(isBalanced(s))

    return result

def isBalanced(s):
    if not s:
        return 'NO'

    closing = {')':'(',']':'[','}':'{'}
    stack = []
    stack_len = 0

    for char in s:
        if char not in closing:
            stack.append(char)
            stack_len += 1
        else:
            if stack_len <= 0:
                return 'NO'

            if stack[-1] == closing[char]:
                stack.pop()
                stack_len -= 1
            else:
                return 'NO'
    
    if len(stack) > 0:
        return 'NO'

    return 'YES'

print(isBalanced(']}'))
