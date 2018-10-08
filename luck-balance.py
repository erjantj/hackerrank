def luckBalance(k, contests):
    result = 0
    importanceCount = {}
    importants = []

    for contest in contests:
        if contest[1] == 1:
            importants.append(contest[0])
            importanceCount[contest[0]] = importanceCount.get(contest[0], 0) + 1
        else:
            result += contest[0]

    importants = sorted(importants)  

    counter = 0
    for i in range(len(importants)-1, -1, -1):
        important = importants[i]
        if counter < k:
            result += important
        else:
            result -= important

        counter += 1

    return result


k = 3 
contests = [[5, 1], [2, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]]
print(luckBalance(k, contests))