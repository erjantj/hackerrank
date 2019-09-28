def searchInSortedMatrix(matrix, target):
    if not matrix:
        return [-1,-1]
    
    i = 0
    j = len(matrix[0]) - 1
    
    while i < len(matrix) and j >= 0:
        print(matrix[i][j])
        if target == matrix[i][j]:
            return [i,j]
        elif target < matrix[i][j]:
            j -= 1
        elif target > matrix[i][j]:
            i += 1
    return [-1,-1]
    


matrix = [
    [1,4,7,12,15,1000],
    [2,5,19,31,32,1001],
    [3,8,24,33,35,1002],
    [40,41,42,44,45,1003],
    [99,100,103,106,128,1004]
]
target = 44

print(searchInSortedMatrix(matrix, target))