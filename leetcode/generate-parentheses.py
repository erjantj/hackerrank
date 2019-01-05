def helper(n, arr, s='', open_ones = 0, closed_ones = 0):
    if len(s) >= n*2:
        print(s)
        arr.append(s)

    if closed_ones < open_ones:
        helper(n, arr, s+')', open_ones, closed_ones+1)
    if open_ones < n:
        helper(n, arr, s+'(', open_ones+1, closed_ones)
    
def generateParenthesis(n):
    arr = []
    helper(n, arr)
    return arr
n=4
print(generateParenthesis(n))