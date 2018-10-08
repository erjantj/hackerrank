# Complete the triplets function below.
def triplets(a, b, c):
    a = sorted(set(a))
    b = sorted(set(b))
    c = sorted(set(c))

    bi = 0
    ai = 0
    ci = 0
    a_len = len(a)
    b_len = len(b)
    c_len = len(c)

    print(a)
    print(b)
    print(c)

    summ = 0
    while bi < b_len:
        print(b[bi])
        while ai < a_len and a[ai] <= b[bi]:
            print('a', b[bi], a[ai])
            ai += 1

        while ci < c_len and c[ci] <= b[bi]:
            print('c', b[bi], c[ci])
            ci += 1

        summ += ai*ci
        
        bi += 1

    return summ


print(triplets([1,4,5],[2,3,3],[1,2,3]))