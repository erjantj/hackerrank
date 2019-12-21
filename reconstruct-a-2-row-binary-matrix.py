class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum):
        if sum(colsum) != upper + lower:
            return []

        order_changed=False
        if upper > lower:
            order_changed = True
            upper, lower = lower, upper

        upper_list = [None for i in range(len(colsum))]
        lower_list = [None for i in range(len(colsum))]

        for i in range(len(colsum)):
            if colsum[i] == 2:
                upper_list[i] = 1
                lower_list[i] = 1
                upper -= 1
                lower -= 1
            elif colsum[i] == 0:
                upper_list[i] = 0
                lower_list[i] = 0

        if upper < 0 or lower < 0:
            return []

        for i in range(len(colsum)):
            if upper_list[i] == None:
                if upper > 0:
                    upper_list[i] = 1
                    lower_list[i] = 0
                    upper -= 1
                else:
                    upper_list[i] = 0
                    lower_list[i] = 1

        if order_changed:
            return [lower_list, upper_list]
        return[upper_list,lower_list]

upper = 2
lower = 1
colsum = [1,1,1]

# upper = 2
# lower = 3
# colsum = [2,2,1,1]

# upper = 5
# lower = 5
# colsum = [2,1,2,0,1,0,1,2,0,1]

print(Solution().reconstructMatrix(upper, lower, colsum))

[[1,1,1,0,1,0,0,1,0,0],[1,0,1,0,0,0,1,1,0,1]]

[[1,1,1,0,1,0,0,1,0,0],[1,0,1,0,0,0,1,1,0,1]]