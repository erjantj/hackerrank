def binarySearchPosition(sums, index):
    left = 0
    right = len(sums) - 1

    while left < right:
        mid = (left+right)//2
        if sums[mid] == index:
            left = mid
            break
        elif sums[mid] > index:
            right = mid-1
        elif sums[mid] < index:
            left = mid+1

    return left

def findRage(s, slots):
    arr = []
    sums = [0]
    int_start = 48
    int_end = 57
    tmp_int = None

    for i in range(len(s)):
        c_parsed = ord(s[i])

        if c_parsed >= int_start and c_parsed <= int_end:
            if tmp_int == None:
                tmp_int = 0
            tmp_int = tmp_int*10 + (c_parsed-int_start)
        else:
            if tmp_int == None:
                arr.append(1)
            else:
                arr.append(tmp_int)
                tmp_int = None
                

    for i in range(1, len(arr)+1):
        sums.append(sums[i-1]+arr[i-1])

    slot = [1, 7]
    print(arr)
    print(sums)
    slot_start = binarySearchPosition(sums, slot[0])
    slot_end = binarySearchPosition(sums, slot[1])

    if slot_start == slot_end:
        print(arr[slot_start-1])
    else:
        print(slot_start-1, slot_end-1)
        leftover_start = slot[0]-arr[slot_start-1]
        leftover_end = arr[slot_end-1]
        if sums[slot_end] != sums[-1]:
            leftover_end = arr[slot_end-1]-(slot[1]-arr[slot_end-1])
        leftover_between  = sums[slot_end-1]-sums[slot_start-1]
        # total = leftover_start+leftover_between+leftover_end
        print(leftover_start, leftover_between, leftover_end)

s = "a2bc3a"
slots = [
    [1,7],
    [5,7],
    [1,2],
    [3,5],
    [4,4],
]

# s = "a2b10cb3a"
# slots = [
#     [1,7],
#     [5,7],
#     [1,2],
#     [3,5],
#     [4,4],
# ]

print(findRage(s, slots))


# a2bc3a
# abbcaaa
# 
# abbcaaa (1,7)
# abbc aaa  (5,7)
# ab bca aa (3,5)

# [1, 2, 1, 3]
#  ^        ^
#  1        7        
# [0, 1, 3, 4, 7]
#              ^