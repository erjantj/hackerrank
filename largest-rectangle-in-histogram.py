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

heights = [2,3,5,6,2,3]
# heights = [3,2,6,5,1,2]
# heights = [5,6,7,6,3,5,7,8,6]
# heights = [6,8,7,5,3,6,7,6,5]

print(largestRectangleArea(heights))
