def count_sort(arr, n):
    arr_len = len(arr)
    tmp = [0]*(n+1)
    sortedd = [0]*(arr_len+1)

    for i in range(arr_len):
        tmp[arr[i]] += 1

    for i in range(1, n+1):
        tmp[i] += tmp[i-1]

    tmp = [0]+tmp
    for i in range(arr_len):
        sortedd[tmp[arr[i]]] = arr[i]
        tmp[arr[i]]+=1

    return sortedd[:arr_len]


with open('input.txt') as f:
    content = f.readlines()
    n = int(content[0])

    k = 1
    half = n//2
    letters = {}
    for i in range(n):
        x, s = content[k].split()        
        x = int(x)
        if i < half:
            s = '-'
        k += 1

        if x not in letters:
            letters[x] = []

        letters[x].append(s)

    sortedd = count_sort(list(letters.keys()), 100)

    for i in sortedd:
        for c in letters[i]:
            print(c, end =' ')