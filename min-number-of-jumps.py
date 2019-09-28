import sys

def minNumberOfJumps(array):
    if not array:
        return 0
    jumps = 0
    max_reach = array[0]
    steps = array[0]

    for i in range(len(array)):
        max_reach = max(max_reach, array[i]+i)
        steps -= 1

        if steps == 0:
            steps += max_reach-i
            jumps += 1

    return jumps+1

array = [3,4,2,1,2,3,7,1,1,1,3]
array = [1,7,0,0,3,0]
print(minNumberOfJumps(array))