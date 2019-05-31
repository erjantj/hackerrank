def helper(arr):
    result = []
    count = 1
    prev_item = arr[0]

    for i in range(1, len(arr)):
        if arr[i] != prev_item:
            result.append(count)
            result.append(prev_item)
            count = 0
        count+= 1
        prev_item = arr[i]

    result.append(count)
    result.append(prev_item)

    return result

def lookAndSayQueries(qs):
    result = []
    memo = {1: [1]}

    for q in qs:
        arr = [1]
        if q in memo:
            arr = memo[q]
        else:
            for i in range(1,q):
                arr = helper(arr)
                memo[i+1] = arr

        result.append(sum(arr))
    return result
    

q = [1,2,5]
print(lookAndSayQueries(q))