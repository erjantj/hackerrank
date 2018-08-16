def substrCount(n, s):
    s = s+'*'
    arr = []
    row = ['', 0]
    polindromes = 0

    for i in range(n+1):
        c = s[i]

        if c == row[0]:
            row[1] += 1

        if c != row[0]:
            if row[0]:
                arr.append(row)
            row = [c, 1]

    
    for row in arr:
        polindromes += (row[1]*(row[1]+1))//2

    for i in range(1,len(arr)-1):
        if arr[i-1][0] == arr[i+1][0] and arr[i][1] == 1:
            polindromes += min(arr[i-1][1],arr[i+1][1])

    return polindromes


with open('input.txt') as f:
    content = f.readlines()
    n = int(content[0])
    s = content[1].strip()

    print(substrCount(n,s))
