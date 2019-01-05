def printMatrix(matrix):
    for row in matrix:
        print(row)
    print()

def rotate(matrix):
    n = len(matrix[0])
    for offset in range(n//2):
        for i in range(0,n-(offset*2)-1):
            # t
            carry = matrix[offset][i+offset]

            # r
            matrix[offset+i][n-1-offset], carry = carry, matrix[offset+i][n-1-offset]

            # b
            matrix[n-1-offset][n-1-i-offset], carry = carry, matrix[n-1-offset][n-1-i-offset]

            # l
            matrix[n-1-i-offset][offset], carry = carry, matrix[n-1-i-offset][offset]

            # t
            matrix[offset][i+offset], carry = carry, matrix[offset][i+offset]

matrix = [
    [1,2],
    [4,5]
]

# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# matrix = [
#     [ 5, 1, 9,11],
#     [ 2, 4, 8,10],
#     [13, 3, 6, 7],
#     [15,14,12,16]
# ]

# matrix = [
#     [ 5, 2,  1,  9, 11],
#     [ 2, 3,  4,  8, 10],
#     [13, 4,  3,  6,  7],
#     [15, 5, 14, 12, 16],
#     [ 5, 3,  2,  8,  0]
# ]

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

printMatrix(matrix)
rotate(matrix)
printMatrix(matrix)