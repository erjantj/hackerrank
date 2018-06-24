def count_sort(arr, arr_len, memo):
    tmp = [0]*201
    sortedd = [0]*(arr_len+1)

    for i in range(arr_len):
        memo[arr[i]] += 1

    for i in range(1, 201):
        tmp[i] = memo[i]
        tmp[i] += tmp[i-1]
    
    tmp = [0]+tmp
    for i in range(arr_len):
        sortedd[tmp[arr[i]]] = arr[i]
        tmp[arr[i]]+=1

    return sortedd[:arr_len]

def count_sort2(sortedd, k, arr_len, memo):
    tmp = [0]*201
    memo[k] += 1
    
    for i in range(1, 201):
        tmp[i] = memo[i]
        tmp[i] += tmp[i-1]

    sortedd = [0]+sorted
    sortedd[tmp[k]-1] = k

    return sortedd[:arr_len]


def get_median(arr, n):
    if n%2 == 1:
        return  arr[n//2]
    else:
        return (arr[n//2]+arr[n//2-1])/2


with open('input.txt') as f:
    content = f.readlines()
    n, d = [int(x) for x in content[0].split()]
    arr = [int(x) for x in content[1].split()]

    notify = 0
    memo = [0]*201

    period = arr[:d]
    sorted = count_sort(period, d, memo)
    print(sorted)

    print('---')
    sorted = count_sort2(sorted, 1, d, memo)
    print(sorted)
    # for i in range(n-d):
    # #     trailing = arr[i+d]
    #     sortedd = count_sort(period, d, tmp)
    # #     median = get_median(sorted, d)
        
    # #     if median*2 <= trailing:
    # #         notify += 1 
                
    # #     del sorted[0]
    # #     sorted.append(trailing)
    # #     period = sorted



    

    # # print(notify)