def test(a):
    if not a:
        return 0

    dp = {a[0]}

    for i in range(1, len(a)):
        x = a[i]
        dp_tmp = []
        dp_remove = []
        for y in dp:
            dp_remove.append(y)
            dp_tmp.append(abs(x-y))

        for y in dp_remove:
            dp.remove(y)
        for y in dp_tmp:
            dp.add(y)


        print(x)
        print(dp)

    return min(dp)


a = [2,7,4,1,8,1]
print(test(a))