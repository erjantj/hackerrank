def fillRow(matrix, row):
    for i in range(1, len(matrix[0])):
        if matrix[row][i] != 0:
            matrix[row][i] = '.'

def fillCol(matrix, col):
    for i in range(1,len(matrix)):
        if matrix[i][col] != 0:
            matrix[i][col] = '.'

def setZeroes(matrix):
    if not matrix:
        return 

    m = len(matrix)
    n = len(matrix[0])
    
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                if not isinstance(matrix[0][j], list) or \
                    (isinstance(matrix[0][j], list) and matrix[0][j][0] != '*'):
                    fillCol(matrix, j)
                    if not isinstance(matrix[0][j], list):
                        matrix[0][j] = [0,0]
                    matrix[0][j][0] = '*'

                if not isinstance(matrix[i][0], list) or \
                    (isinstance(matrix[i][0], list) and matrix[i][0][1] != '*'):
                    fillRow(matrix, i)
                    if not isinstance(matrix[i][0], list):
                        matrix[i][0] = [0,0]
                    matrix[i][0][1] = '*'


    for i in range(m):
        for j in range(n):
            if matrix[i][j] == '.' or isinstance(matrix[i][j], list):
                matrix[i][j] = 0
                    
                


matrix = [
  [1,1,1],
  [1,0,1],
  [1,1,1]
]

# matrix = [
#     [0,1,2,0],
# ]


# matrix = [
#   [0,1,2,0],
#   [3,4,5,2],
#   [1,3,1,5]
# ]

# matrix = [
#     [8,3,6,9,7,8,0,6],
#     [0,3,7,0,0,4,3,8],
#     [5,3,6,7,1,6,2,6],
#     [8,7,2,5,0,6,4,0],
#     [0,2,9,9,3,9,7,3]
# ]


# matrix = [
#     [0,0,0,5],
#     [4,3,1,4],
#     [0,1,1,4],
#     [1,2,1,3],
#     [0,0,1,1]
# ]

# matrix = [
#     [0,1,2,0],
#     [3,4,5,2],
#     [1,3,1,5]
# ]

for row in matrix:
    print(row)

print(setZeroes(matrix))

for row in matrix:
    print(row)