def largestRectangleArea(heights):
    if not heights:
        return 0

    stack = [-1]
    heights.append(0)
    result = 0

    for i in range(len(heights)):
        while stack and heights[i] < heights[stack[-1]]:
            last_index = stack.pop()
            h = heights[last_index]
            w = i-stack[-1]-1

            result = max(result, h*w)

        stack.append(i)

    return result

def maximalRectangle(matrix):
    if not matrix:
        return 0
        
    histogram = [0]*len(matrix[0])
    result = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == "1":
                if i == 0 or matrix[i-1][j] == "0":
                    histogram[j] = 1
                else:
                    histogram[j] += 1
            else:
                histogram[j] = 0
        result = max(result, largestRectangleArea(histogram))

    return result

# matrix = [
#   ["1","0","1","0","0"],
#   ["1","0","1","1","1"],
#   ["1","1","1","1","1"],
#   ["1","0","0","1","0"]
# ]


matrix = [
  ["1","0","1","0","0"],
  ["1","1","1","0","1"],
  ["1","1","1","1","1"],
  ["0","0","0","1","0"]
]

matrix = [
   ["1","0"],
   ["1","0"]
]

print(maximalRectangle(matrix))