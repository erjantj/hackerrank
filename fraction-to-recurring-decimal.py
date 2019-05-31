import math, time

def get_int_len(n):
    digits = 0

    if n > 0:
        digits = int(math.log10(n))+1
    elif n == 0:
        digits = 1
    else:
        digits = int(math.log10(-n))+2 

    return digits

def fractionToDecimal(n, d):
    result_arr = []
    result = []
    reminder_len = get_int_len(n)-1
    reminder = n//10**(reminder_len)
    n = n%10**(reminder_len)
    candidate_locations = {}
    track_fraction = False
    mutiplier = 1
    found_crecurring = False
    borrow_len = 0

    while(reminder):
        candiadate_index = len(result_arr)
        print(reminder, n, reminder_len, borrow_len)

        if reminder >= d:
            candiadate = reminder//d
            tmp_sub = candiadate*d
            reminder = reminder - tmp_sub
        else:
            candiadate = 0
            if not track_fraction and reminder_len <= 0:
                track_fraction = True
                if not result_arr:
                    result_arr.append(0)
                candiadate = ','
            else:
                if reminder_len>0:
                    reminder_len = reminder_len - 1 
                    reminder = reminder*10 + n//10**(reminder_len)
                    n = n%10**(reminder_len)  
                else:
                    borrow_len += 1
                    continue

        # if candiadate in candidate_locations:
        #     found_crecurring = True
        #     result_arr.append(candiadate)
        #     break
        
        result_arr.append(candiadate)
        if track_fraction:
            candidate_locations[candiadate] = candiadate_index

        print(result_arr)
        time.sleep(1)



    # start_index = candidate_locations[candiadate]
    # for i in range(len(result_arr)):
    #     if found_crecurring:
    #         if i == start_index:
    #             result.append('(')
    #     result.append(str(result_arr[i]))

    # if found_crecurring:
    #     result.append(')')

    # return ''.join(result)
n = 40
d = 333

# n = 4
# d = 33

# n = 40
# d = 33

# n = 1
# d = 2

print(fractionToDecimal(n,d))