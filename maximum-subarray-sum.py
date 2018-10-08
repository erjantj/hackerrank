def maximumSum(a, m):
    a_len = len(a)
    sums = [0]*a_len
    sums[0] = a[0]
    maxx = a[0]%m

    for i in range(1, a_len):
        sums[i] += sums[i-1]+a[i]
        if maxx < i%m:
            maxx = i%m

    for i in range(0, a_len-1):
        for j in range(i+2, a_len+1):
            lower = 0
            upper = sums[a_len-1]

            if i > 0:
                lower = sums[i-1]
            if j < a_len:
                upper = sums[j-1]

            if maxx < (upper-lower)%m:
                maxx = (upper-lower)%m

    return maxx
a = [3,3,9,9,5]
m = 7

print(maximumSum(a,m))
