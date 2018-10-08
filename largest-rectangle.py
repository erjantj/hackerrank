def largestRectangle(h):
    stack = []
    h.append(0)
    h_len = len(h)
    result = h_len

    for i in range(h_len):
        last_index = i
        while len(stack) > 0 and h[i] < stack[-1][0]:
            last = stack.pop()
            last_index = last[1]

            result = max(result, (h[i]*(i-last_index+1)))
            result = max(result, (last[0]*(i-last_index)))

        stack.append((h[i], last_index))

    return result

h = [3,6,4]

print(largestRectangle(h))
