def threeNumberSum(array, targetSum):
    n = len(array)
    if n < 3: return []
    if n == 3 and sum(array) == targetSum: return [array]
    
    result = []
    array.sort()
    for i in range(n):
        index = set()
        for j in range(i+1,n):
            k = targetSum - (array[i]+array[j])
            if array[j] in index:
                result.append([array[i], array[j], k])
            else:
                index.add(k)


    return result

array = [1,2,-1,2,-4,10,5,3,4,-6,8]
targetSum = 7
print(threeNumberSum(array, targetSum))