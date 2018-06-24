# Complete the whichSection function below.
def whichSection(n, k, a):
    currGroup = 0
    currStudents = 0
    a_len = len(a)

    while currStudents < n and currStudents < n:
        if k <= currStudents:
            return currGroup
        currStudents += a[currGroup]
        currGroup = (currGroup+1)%a_len

    return a_len

print(whichSection(470, 1, [11,24,420,6,9]))