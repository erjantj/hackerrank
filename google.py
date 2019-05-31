def helper(arr, i, next_bracket, tmp_result, result):
    if next_bracket >= len(arr):
        result.append(''.join(tmp_result))
        return 
    
    if not arr[next_bracket]:
        helper(arr, i, next_bracket+1, tmp_result, result)

    for j in range(len(arr[next_bracket])):
        tmp_result.append(arr[next_bracket][j])
        helper(arr, j, next_bracket + 1, tmp_result, result)
        tmp_result.pop()

def expandBrackets(s):
    if not s:
        return ''

    arr_index = {}
    k = 0
    for i in range(len(s)):
        if s[i] == '{':
            arr_index[i+1] = [i+1]
            k = i+1 
        elif s[i] == '}':
            arr_index[k].append(i)
    
    arr = []
    for index, vals in arr_index.items():
        if vals:
            arr.append(s[vals[0]:vals[1]].split(','))

    if not arr:
        return ''


    next_bracket = 1
    result = []
    tmp_result = []

    for i in range(len(arr[0])):
        tmp_result.append(arr[0][i])
        helper(arr, i, next_bracket, tmp_result, result)
        tmp_result.pop()

    return ' '.join(result)


s = '{a,b,c}{}{a,b}'

print(expandBrackets(s))