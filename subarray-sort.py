def subarraySort(array):

    minn = max(array)
    maxx = min(array)
    sorted = True
    for i in range(len(array)-1):
        if array[i] > array[i+1]:
            sorted = False
            minn = min(array[i+1], minn)
            maxx = max(array[i], maxx)
    if sorted:
        return [-1,-1]

    l = 0
    r = len(array)-1
    while l < len(array) and minn >= array[l]:
        l += 1
    while r >= 0 and maxx <= array[r]:
        r -= 1

    return [l,r]


