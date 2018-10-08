def find_subarray(arr, s):
    arr_len = len(arr)
    sums = [0]*(arr_len+1)
    sums_indexes = {}
    sums_indexes[0-s] = arr_len

    for i in range(arr_len-1, -1, - 1):
        sums[i] = sums[i+1] + arr[i]
        sums_indexes[sums[i]-s] = i
    print(sums)
    print(sums_indexes)
    for i in range(0,arr_len+1):
        if sums[i] in sums_indexes:
            j = sums_indexes[sums[i]]
            print(j+1, i)
            return

    print(-1)



s = 9
arr = [5,1,2,6,3,4]
# arr = [7,9,4,3,22]
# arr = [1,2,3,7,5]
# arr = [1,3,3,7,5]
# arr = [1,2,3,4,5,6,7,8,9,10]
# arr = [142,112,54,69,148,45,63,158,38,60,124,142,130,179,117,36,191,43,89,107,41,143,65,49,47,6,91,130,171,151,7,102,194,149,30,24,85,155,157,41,167,177,132,109,145,40,27,124,138,139,119,83,130,142,34,116,40,59,105,131,178,107,74,187,22,146,125,73,71,30,178,174,98,113]
print(find_subarray(arr,s))

