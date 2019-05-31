def mySqrt(x: int) -> int:
    if x == 0:
        return 0
    
    if x == 1:
        return 1

    if x == 2:
        return 1

    if x == 3:
        return 1
            
    start = 0
    end = x
    ans = 0
    while start <= end:
        mid = (start+end)//2
        if mid**2 == x:
            ans = mid
            break
        elif mid**2 < x:
            start = mid+1
            ans = mid
        elif mid**2 > x:
            end = mid-1
    return ans


print(mySqrt(257))
