def countAndSay(s):
    count = 0
    prev_c = ''
    q = []

    s += " "
    for c in s:
        if prev_c and c != prev_c:
            q.append(str(count))
            q.append(str(prev_c))
            count = 0      
        prev_c = c 
        count += 1

    return "".join(q)

a = ['1']

for i in range(1,30):
    a.append(countAndSay(a[i-1]))

print(a)    