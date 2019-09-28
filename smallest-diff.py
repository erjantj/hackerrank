import sys

def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()

    result = []
    min_diff = sys.maxsize
    
    l1 = 0
    l2 = 0

    while l1 < len(arrayOne) and l2 < len(arrayTwo):
        diff = abs(arrayOne[l1]-arrayTwo[l2])
        if diff < min_diff:
            min_diff = diff
            result = [arrayOne[l1], arrayTwo[l2]]
            
        if arrayOne[l1] == arrayTwo[l2]:
            break
        elif arrayOne[l1] < arrayTwo[l2]:
            l1 += 1
        else:
            l2 += 1
    
    return result 
    


arrayOne = [-1,5,10,20,28,3]
arrayTwo = [26,134,135,15,17]
print(smallestDifference(arrayOne, arrayTwo))