def helper(pi, numbers, i, memo):
    if i >= len(pi):
        return -1, True

    if i in memo:
        return memo[i]

    min_spaces = len(pi)
    finished = False
    for j in range(len(pi)):
        if pi[i:j+1] in numbers:
            next_spaces, next_finished = helper(pi, numbers, j+1, memo)
            min_spaces = min(min_spaces, next_spaces+1)
            finished = finished or next_finished

    memo[i] = (min_spaces, finished)
    return memo[i]

def numbersInPi(pi, numbers):
    numbers = set(numbers)
    min_spaces, finished = helper(pi, numbers, 0, {})
    if not finished:
        return -1
    return min_spaces


pi = '78324821'
numbers = ['78324', '82', '78', '324', '1']
print(numbersInPi(pi, numbers))
