def fourNumberSum(array, targetSum):
    if not array or len(array) < 4:
        return []

    array.sort()
    result = []
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            l = j+1
            r = len(array) - 1
            while l < r:
                summ = sum([array[i], array[j], array[l], array[r]])
                if summ > targetSum:
                    r -= 1
                elif summ < targetSum:
                    l += 1
                else:
                    result.append([array[i], array[j], array[l], array[r]])
                    r -= 1
                    l += 1

    return result


array = [7,6,4,1,2]
targetSum = 18
print(fourNumberSum(array, targetSum))