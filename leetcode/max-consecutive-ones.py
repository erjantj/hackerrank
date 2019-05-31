def longestOnes(A, K) -> int:
        max_len = 0
        i = 0
        while i < len(A):
            k_tmp = K
            len_tmp = 0
            
            # Search left
            for j in range(i, -1, -1):
                if A[j] == 0:
                    if k_tmp == 0:
                        j -= 1 
                        break
                    k_tmp -= 1
                len_tmp += 1
            
            if len_tmp > max_len:
                max_len = len_tmp
            
            # Search right
            for j in range(i+1, len(A)):
                if A[j] == 0:
                    if k_tmp == 0 and A[j-len_tmp] == 0:
                        k_tmp += 1
                        len_tmp -= 1
                    if k_tmp == 0:
                        j -= 1 
                        break
                    k_tmp -= 1
                len_tmp += 1
                
                if len_tmp > max_len:
                    max_len = len_tmp
            if j >= i:
                i = j
            i += 1

        return max_len

a = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3

# a = [0,0,1,0,1,0,1]
# k = 3


a = [0,0,1,1,1,1,1,1,0,0,0,1,0,1,0,0,0,0,0]
k = 5

print(longestOnes(a, k))