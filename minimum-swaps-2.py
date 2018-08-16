from random import randrange
def count_steps(arr, n):
    swaps = 0
    indexes = {}

    for i in range(n):
        indexes[arr[i]] = i

    for i in range(n):
        if arr[i] != i+1:
            a = indexes[i+1]
            arr[a],arr[i] = arr[i],arr[a]
            indexes[arr[i]],indexes[arr[a]] = indexes[arr[a]],indexes[arr[i]]
            swaps += 1

    return swaps


with open('out.test') as f:
    content = f.readlines()
    n = int(content[0].strip())
    arr = [int(x) for x in content[1].strip().split()]

    print(count_steps(arr, n))

