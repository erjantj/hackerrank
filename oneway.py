def isOneway(s1, s2):
    if len(s1) < len(s2):
        s2,s1 =  s1,s2

    if len(s1) - len(s2) > 1:
        return False

    i1 = 0
    i2 = 0
    edit_distance = 0

    while i1 < len(s1) and i2 < len(s2):
        if s1[i1] == s2[i2]:
            i1 += 1
            i2 += 1
        else:
            if len(s1) == len(s2):
                i1 += 1
                i2 += 1
            else:
                i1 += 1  

            edit_distance += 1

    return edit_distance <= 1




s1 = 'as'
s2 = 'ass'
print(isOneway(s1, s2))

print((isOneway('pale', 'ple') == True))
print((isOneway('pales', 'pale') == True))
print((isOneway('pale', 'bale') == True))
print((isOneway('paleabc', 'pleabc') == True))
print((isOneway('pale', 'ble') == False))
print((isOneway('a', 'b') == True))
print((isOneway('', 'd') == True))
print((isOneway('d', 'de') == True))
print((isOneway('pale', 'pale') == True))
print((isOneway('pale', 'ple') == True))
print((isOneway('ple', 'pale') == True))
print((isOneway('pale', 'bale') == True))
print((isOneway('pale', 'bake') == False))
print((isOneway('pale', 'pse') == False))
print((isOneway('ples', 'pales') == True))
print((isOneway('pale', 'pas') == False))
print((isOneway('pas', 'pale') == False))
print((isOneway('pale', 'pkle') == True))
print((isOneway('pkle', 'pable') == False))
print((isOneway('pal', 'palks') == False))
print((isOneway('palks', 'pal') == False))
