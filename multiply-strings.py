def toInt(s):
    zero = ord('0')
    val = 0
    for c in s:
        val = (val*10) + (ord(c)-zero)


    return val

s = "123"
print(toInt(s))