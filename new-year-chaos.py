def count_steps(arr, n):
    is_sorted = False
    swaps = [2]*(n+1)
    swapsCount = 0
    while not is_sorted:
        is_sorted = True
        lastSorted = n-1

        for i in range(lastSorted):
            if arr[i] > arr[i+1]:
                swapsCount += 1
                swaps[arr[i]] -= 1
                if swaps[arr[i]] < 0:
                    return -1
                arr[i],arr[i+1]=arr[i+1],arr[i]
                is_sorted = False
        lastSorted -= 1

    return swapsCount


with open('input.txt') as f:
    content = f.readlines()
    t = int(content[0].strip())

    k = 1
    for i in range(t):
        n = int(content[k].strip())
        k += 1

        arr = [int(x) for x in content[k].strip().split()]
        k += 1

        result = count_steps(arr, n)

        if result >= 0:
            print(result)
        else:
            print('Too chaotic')
