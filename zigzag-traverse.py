def zigzagTraverse(array):
    result = []
    n = len(array)
    m = len(array[0])
    i = j = 0
    direction = 1
    while len(result) < n*m:
        result.append(array[i][j])
        i+=direction
        j-=direction
        if i < 0 or i >= n or j < 0 or j >= m:
            direction = -direction
        if j < 0 and i >= n:
            j += 2
            i = n-1
        elif i < 0 and j >= m:
            i += 2
            j = m-1
        elif j < 0:
            j = 0
        elif i < 0:
            i = 0
        elif i >= n:
            i = n-1
            j += 2
        elif j >= m:
            j = m-1
            i += 2            
    return result

array = [
    [1,3,4,10],
    [2,5,9,11],
    [6,8,12,15],
    [7,13,14,16],
]

# array = [
#     [1,3,4],
#     [2,5,9],
#     [6,8,10],
#     [7,11,12]
# ]

# array = [
#     [1,3,4],
#     [2,5,6],
# ]

# array = [
#     [1,3,4,7,8],
#     [2,5,6,9,10],
# ]

# array = [
#     [1,3],
#     [2,4],
#     [5,7],
#     [6,8],
# ]

# array = [
#     [1,2,3]
# ]

print(zigzagTraverse(array))

