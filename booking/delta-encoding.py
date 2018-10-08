def delta_encode(arr):
    arr_len = len(arr)
    prev = arr[0]
    token = -128
    result = []
    for i in range(arr_len):
        if i == 0:
            result.append(arr[0])
        else:
            delta = arr[i]-prev
            if delta > 127 or delta < -127:
                result.append(token)
            result.append(delta)
            prev = arr[i]

    return result

arr = [25626,25757,24367,24267,16,100,2,7277]

delta_encode(arr)