def validateStackSequences(pushed, popped):
    if not pushed and popped:
        return False

    if not popped:
        return True

    i = 0
    j = 0
    arr = [pushed[i]]

    while i >= 0 and i < len(pushed) and j >= 0 and j < len(popped):
        if arr and arr[-1] == popped[j]:
            arr.pop()
            j += 1
        else:
            i += 1
            if i < len(pushed):
                arr.append(pushed[i])

    if i >= len(pushed) and j < len(popped):
        return False

    return True
            

pushed = [1,2,3,4,5]
popped = [4,5,3,2,1]

pushed = [1,2,3,4,5]
popped = [4,3,5,1,2]

pushed = [1,2,3,4,5]
popped = []

pushed = []
popped = [1,2,3,4,5]

pushed = []
popped = []

pushed = [1,0]
popped = [1,1]
print(validateStackSequences(pushed, popped))