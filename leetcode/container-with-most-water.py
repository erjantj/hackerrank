def maxArea(h):
    h_len = len(h)
    result = 0

    if h_len < 2:
        return 0

    left = 0 
    right = h_len-1

    while left < right:
        span = right - left
        lower_bound = min(h[right], h[left])
        result = max(result, span*lower_bound)

        if h[left] < h[right]:
            left += 1
        else:
            right -=1

    return result


height = [2,3,10,5,7,8,9]
        # 0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 
# height = [1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]
# height = [1,8,6,2,5,4,8,3,7]
# height = [7,3,8,4,5,2,6,8,1]
# height = [3,2,5,4]
# print(maxArea(height))
# print('--')
# height = [4,8,2,5]
print(maxArea(height))