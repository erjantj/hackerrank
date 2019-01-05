def isMatch(s, p):
    pr = ''
    sp = ''
    i = 0
    j = 0
    star = '*'
    dot = '.'
    ss = list(s)
    pp = list(p)

    while i < len(pp) or j < len(ss):
        if i >= len(pp) and j >= len(ss):
            return True
        else:
            if i >= len(pp):
                print('asd')
                if sp == star:
                    return True
                if not sp == star:
                    return False
            if j >= len(ss):
                if sp == star:
                    return True
                if not sp == star:
                    return False
                

        print('pi=',pp[i])
        print('sj=',ss[j])
        print('pr=',pr)
        print('sp=',sp)
        print()
        

        if sp == star:
            if pr == ss[j]:
                j += 1
            else:
                i += 1
                sp = ''
                pr = ''
        else:
            if pp[i] == star:
                sp = star
                pr = p[i-1]
            elif pp[i] == dot:
                pp[i] = ss[j]
                i += 1
                j += 1
            elif pp[i] != ss[j]:
                if i+1 < len(pp) and pp[i+1] == star:
                    i += 2
                else:
                    return False
            else:
                i += 1
                j += 1

    return True

# s='mississippi'
# p='mis*is*p*.'

s='ab'
p='.*'

print(isMatch(s,p))