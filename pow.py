import sys

def pow(x, n, negative = False, memo = {}):
    if n == 0:
        return 1
    if n == 1:
        return x
    if n == 2:
        return x*x

    key = (x,n)
    if key in memo:
        return memo[key]

    divide = False
    if n < 0:
        negative = True
        divide = True
        n = abs(n)

    result = 0
    if n%2 == 0:
        result = pow(x, n//2, negative, memo)*pow(x, n//2, negative, memo)    
    else:
        result = x*pow(x, n-1, negative, memo)

    if negative and result >= sys.maxsize:
        return 0

    if divide and result > 0:
        return 1/result

    memo[key] = result
    return memo[key]


# print(pow(0.00001, 2147483647))
print(pow(2.00000, 214))
print(2.00000**214)
