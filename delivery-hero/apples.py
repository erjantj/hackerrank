def find_max(a, k, l):
    a_len = len(a)
    max_k = 0
    max_l = 0
    max_total = 0
    tmp_max_k = 0

    if a_len == 0:
        return -1

    if a_len < k+l:
        return -1

    prefix_sum = [0,a[0]]

    for i in range(1, a_len):
        prefix_sum.append(a[i]+prefix_sum[i])

    for i in range(l, a_len-k+1):
        sum_k = prefix_sum[i+k]-prefix_sum[i]
        if sum_k > tmp_max_k:
            tmp_max_k = sum_k
            for j in range(0, a_len-k-l+1):
                sum_l = prefix_sum[j+l]-prefix_sum[j]
                if sum_l > max_l:
                    max_l = sum_l
                    max_total = sum_k + sum_l

    return max_total

a = [6,1,4,6,3,2,7,4]
k = 3 
l = 3
print(find_max(a, k, l))
