def maxSumIncreasingSubsequence(array):
    if not array:
        return [0, []]
    max_sum_index = 0
    sums = [array[0]]
    sums_indexes = [None]

    for i in range(1, len(array)):
        tmp_sum = array[i]
        tmp_index = None
        for j in range(i):
            if array[j] < array[i] and sums[j]+array[i] > tmp_sum:
                tmp_sum = sums[j]+array[i]
                tmp_index = j
        if tmp_sum > sums[max_sum_index]:
            max_sum_index = i
        sums.append(tmp_sum)
        sums_indexes.append(tmp_index)

    index = max_sum_index
    result = []
    while index != None:
        result.append(array[index])
        index = sums_indexes[index]
    result.reverse()

    return [sums[max_sum_index], result]
    



# array = [1,2,4,0,5,3,4,5,2,4]
# array = [10,70,20,30,50,11,30]
# array = [6,5,4,3,2,1]
# array = [-5,-1,-6,-5,-4,-3]
print(maxSumIncreasingSubsequence(array))