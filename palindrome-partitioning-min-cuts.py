def palindromePartitioningMinCuts(string):
    if not string or len(string) == 1:
        return 0

    result = [float('inf') for i in range(len(string))]
    polindromes = [[False for i in range(len(string))] for i in range(len(string))]
    for i in range(len(string)):
        polindromes[i][i] = True

    for length in range(2, len(string)+1):
        for i in range(len(string)-length+1):
            j = i+length-1
            if string[i] == string[j]:
                polindromes[i][j] = True if length==2 or polindromes[i+1][j-1] else False


    result[0] = 0
    for i in range(1, len(string)):
        for j in range(i+1):
            if polindromes[j][i]:
                if j-1 < 0:
                    result[i] = 0
                else:
                    result[i] = min(result[j-1]+1, result[i])
                print(string[:i+1], result[i])


    return result[len(string)-1]


string = 'noonabbad'
string = 'asdfgh'
# string = 'a'
print(palindromePartitioningMinCuts(string))
