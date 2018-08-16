def get_bigger_indexes(indexes, k):
    if not indexes:
        return []

    leftIndex = 0
    rightIndex = len(indexes)-1

    if k >= indexes[-1]:
        return []

    i = (leftIndex + rightIndex) // 2
    while leftIndex <= rightIndex:
        i = (leftIndex + rightIndex) // 2
        if indexes[i] == k:
            return indexes[i+1:]
        elif indexes[i] < k:
            leftIndex = i + 1
        elif indexes[i] > k:
            rightIndex = i - 1
        else:
            return -1

    if indexes[i] < k:
        return indexes[i+1:]
    return indexes[i:]



def countTriplets(arr, r, n):
    memo = {}
    result = 0
    maxItem = 0

    for i in range(n):
        a = arr[i]
        if a==1 or a%r == 0:
            memo[a] = memo.get(a, {})
            memo[a][i] = {'second':[], 'third': []}

            prev = a//r
            prev_prev = a//(r*r)

            prevItem = memo.get(prev, {})
            if prevItem:
                for index, items in prevItem.items():
                    if index < i:
                        items['second'].append(i)


    print(memo)

    startLimit = maxItem//(r*r)
    for i in range(n):
        a = arr[i]
        if a <= startLimit:
            second = a*r
            third = a*r*r

            
    return result

r = 2
arr = [1,2,4,1,4,2,4]

# r = 3
# arr = [1,3,9,9,27,81]

# r = 3
# arr = [1,2,1,6,3,2,6,9,27,18,9,18,9,54]

print(countTriplets(arr, r, len(arr)))

