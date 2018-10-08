def dbValue(value):
    power = 0
    summ = 0
    while value > 0:
        digit = value%10
        value = value//10

        summ += digit*(2**power)

        power += 1

    return summ


test = {}
for i in range(0,520):
    # if i%10 == 0:
    #     print('**',i)
    #     print('---')

    test[i] = dbValue(i)
sorted_by_value = sorted(test.items(), key=lambda kv: kv[1])

for i in range(len(sorted_by_value)):
    print(i, sorted_by_value[i][0], sorted_by_value[i][1])

