def waterArea(heights):
    if not heights:
        return 0
    summ = 0
    n = len(heights)
    l_max = [num for num in heights]
    r_max = [num for num in heights]

    for i in range(1, n):
        j = n-i-1
        l_max[i] = max(l_max[i-1], l_max[i])
        r_max[j] = max(r_max[j+1], r_max[j])

    for i in range(0, n):
        h = min(l_max[i], r_max[i])-heights[i]
        summ += h
    return summ

heights = [0,3,0,8,0,0,5,0,0,10,0,0,1,1,0,3]
heights = [0,8,0,0,5,0,0,10,0,0,1,1,0,3]
heights = [10,0,8,0,10,0,3]
print(waterArea(heights))
