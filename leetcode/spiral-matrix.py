def spiralOrder(matrix):
    if not matrix:
        return []

    m = len(matrix)
    n = len(matrix[0])

    if m == 1:
        return matrix[0]

    offset = 0
    result = []
    k=0
    while k < n*m:

        if k == n*m-1:
            k += 1
            result.append(matrix[offset][i+offset-1])

        for i in range(0,n-(offset*2)-1):
            if k < n*m:
                k += 1
                result.append(matrix[offset][i+offset])
            else:
                break

        for i in range(0,m-(offset*2)-1):   
            if k < n*m:
                k += 1
                result.append(matrix[offset+i][n-1-offset])
            else:
                break

        for i in range(0,n-(offset*2)-1):
            if k < n*m:
                k += 1
                result.append(matrix[m-1-offset][n-1-i-offset])
            else:
                break

        for i in range(0,m-(offset*2)-1):
            if k < n*m:
                k += 1
                result.append(matrix[m-1-i-offset][offset])
            else:
                break

        offset += 1

    return result

    
# matrix = [
#     [1,2],
#     [4,5]
# ]

# matrix = [
#     [1,2,3,4],
#     [4,5,6,5],
#     [7,8,9,6]
# ]

# matrix = [
#     [ 5, 1, 9,11],
#     [ 2, 4, 8,10],
#     [13, 3, 6, 7],
#     [15,14,12,16]
# ]

matrix = [
    [ 5, 2,  1,  9, 11],
    [ 2, 3,  4,  8, 10],
    [13, 4,  3,  6,  7],
    [15, 5, 14, 12, 16],
    [ 5, 3,  2,  8,  0]
]

# matrix = [
#     [ 5, 2,  1,  9, 11, 5],
#     [ 2, 3,  4,  8, 10, 2],
#     [13, 4,  3,  6,  7, 8],
#     [15, 5, 14, 12, 16, 0],
#     [ 5, 3,  2,  8,  0, 1],
#     [ 3, 3,  2,  1,  1, 1]
# ]

# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# matrix = [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
print(spiralOrder(matrix))
