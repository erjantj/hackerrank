def minIncrementForUnique(a):
    if not a :
        return 0
    a = sorted(a)
    unique_set = set()
    memo = {}
    steps = 0

    for i in range(len(a)):
        if not a[i] in unique_set:
            unique_set.add(a[i])
            memo[a[i]] = 0
        else:
            tmp_steps = memo[a[i-1]] - (a[i]-a[i-1]) + 1
            memo[a[i]] = tmp_steps
            steps += tmp_steps
            unique_set.add(a[i]+tmp_steps) 
    return steps
    


a = [3,2,1,2,1,7]
a = [4,4,7,5,1,9,4,7,3,8]
a = [1,1,1,1,1]
print(minIncrementForUnique(a))