import sys

def riddle(arr):
    print(arr)
    print(len(arr))

    arr_len = len(arr)

    max_key = 0
    max_window = {}
    max_window_index = {}
    inverted_max_window = {}
    maxx_array = []

    stack = [0]
    max_window[0] = [1, 1]

    # left max
    for i in range(1, arr_len):
        max_window[i] = max_window.get(i, [1,1])
        while len(stack) > 0 and arr[stack[-1]] >= arr[i]:
            stack.pop()
            if not stack:
                # big from all elements
                max_window[i][0] = max(max_window[i][0], (i+1))
            else:
                max_window[i][0] = max(max_window[i][0], (i - stack[-1]))

        stack.append(i)

    stack = [arr_len-1]
    max_window[arr_len-1][1] = 1

    # right max
    for i in range(arr_len-1,-1,-1):
        while len(stack) > 0 and arr[stack[-1]] >= arr[i]:
            stack.pop()
            if not stack:
                # big from all elements
                max_window[i][1] = max(max_window[i][1], (arr_len-i))
            else:
                max_window[i][1] = max(max_window[i][1], (stack[-1] - i))

        stack.append(i)

    for key, val in max_window.items():
        max_window[key] = val[0]+val[1]-1

    for i, val in max_window.items():
        max_window_index[arr[i]] = max(max_window_index.get(arr[i], 1), val)

    print(max_window_index)
    print()

    for key,val in max_window_index.items():
        inverted_max_window[val] = max(inverted_max_window.get(val, 0), key)
        if val > max_key:
            max_key = val
    
    maxx = inverted_max_window[max_key]
    maxx_array.append(maxx)

    for i in range(arr_len-1, 0, -1):
        if i in inverted_max_window and inverted_max_window[i] > maxx:
            maxx = inverted_max_window[i]
        maxx_array.append(maxx)

    maxx_array_reverse = []
    for i in range(arr_len-1, -1, -1):
        maxx_array_reverse.append(maxx_array[i])

    return maxx_array_reverse

# arr = [3,6,6,6,6,6,10,2,6,6,6,6,6,6,6,3]
# arr = [2,6,1,12]
# arr = [3,5,4,7,6,2]
# arr = [1,2,3,5,1,13,3]
arr = [894, 675, 318, 796, 61, 926, 39, 641, 580, 69, 79, 434, 150]
print(riddle(arr))