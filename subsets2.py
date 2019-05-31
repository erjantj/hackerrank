def helper(a, result, tmp, i):
    if i >= len(a):
        result.append([x for x in tmp if x != None])
        return 


    tmp[i] = None
    helper(a, result, tmp, i+1)
    tmp[i] = a[i]
    helper(a, result, tmp, i+1)

def subsets(a):
    result = []
    
    tmp = [None] * len(a)
    helper(a, result, tmp, 0)    
    return result

a = [1,2,3]
print(subsets(a))