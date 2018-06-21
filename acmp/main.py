file = open("INPUT.TXT","r")
 
res = []
line = file.readline().strip().split()
max_jump = int(line[0])
stairs = int(line[1])
 
for x in range(0,stairs):
    if x < max_jump:
        res.append(2**x)
    else:
        res.append(sum(res))
        del res[0]
file = open("OUTPUT.TXT","w")
file.write(str(res[-1]))