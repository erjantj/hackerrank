def isInt(s, i, found):
    minus_int = ord('-')
    plus_int = ord('+')
    zero_int = ord('0')
    nine_int = ord('9')

    char_int = ord(s[i])
    
    if i < len(s)-1:
        next_char_int = ord(s[i+1])
        if not found and (char_int == minus_int or char_int == plus_int) and (next_char_int < zero_int or next_char_int > nine_int):
            return False

    if not found and i == len(s)-1 and (char_int == minus_int or char_int == plus_int):
        return False

    if found and (char_int == minus_int or char_int == plus_int):
        return False

    if (char_int == minus_int or char_int == plus_int) or (char_int >= zero_int and char_int <= nine_int):
        return True

    return False
    
def myAtoi(s):
    start = 0
    end = 0
    found = False
    minus = False

    for i in range(len(s)):
        if not found and s[i] == ' ':
            continue

        if i < (len(s)-1) and s[i] == '0' and s[i+1] == '0':
            continue


        isItInt = isInt(s, i, found)

        if isItInt and s[i] == '-':
            minus = True

        if not isItInt:
            break
        else:
            if not found and s[i] != 0 and s[i] != '-':
                found = True
                start = i
                end = i
            else:
                end = i

    if not found:
        return 0

    if end-start > 11:
        if minus:
            return -2**31
        else:
            return 2**31-1
    
    result = int(s[start:end+1])    
    if minus:
        result = int(s[start:end+1])*-1    

    if result < -2**31:
        return -2**31

    if result > 2**31-1:
        return 2**31-1

    return result

s = "2147-"
print(myAtoi(s))
