def partitionDisjoint(a):
    a_len = len(a)
    maxL = a[0]
    minR = a[a_len-1]

    i = 0
    j = a_len-1
    middle = 0
    high = a_len

    while i < high and j >= 0:
        print(a[i] <= a[j] , a[j] >= maxL , a[i] <= minR)
        if not (a[i] <= a[j] and a[j] >= maxL and a[i] <= minR):
            if high-(j+1) == 0:
                return j+1
            else:
                high = j+1
                i = 0
                j = high-1
                maxL = a[i]
                minR = a[j]
                continue
            
        i += 1
        j -= 1


a = [1,1,1,1,2,2,2,2]
print(partitionDisjoint(a))