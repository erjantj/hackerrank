def compress(s):
    if not s: 
        return ''

    compressed = False
    tmp_s = ''
    prev_c = ''
    count = 0

    s += " "
    for c in s:
        if prev_c and c != prev_c:
            if count > 1:
                compressed = True
            tmp_s += "%s%d"%(prev_c, count)
            count = 0

        prev_c = c
        count += 1


    if not compressed:
        return s

    return tmp_s



s = 'abc'
print(compress(s))