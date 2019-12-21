def rectangleMania(coords):
    if not coords:
        return 0

    count = 0
    pairs = []
    index = {}

    for point in coords:
        if not point[0] in index:
            index[point[0]] = []
        index[point[0]].append(point)

    for key, group in index.items():
        for i in range(len(group)):
            for j in range(i+1, len(group)):
                pairs.append((group[i], group[j]))


    for i in range(len(pairs)):
        pair1 = pairs[i]
        for j in range(i+1, len(pairs)):
            pair2 = pairs[j]
            if (pair1[0][1] == pair2[0][1] and pair1[1][1] == pair2[1][1]
                ) or (pair1[0][1] == pair2[1][1] and pair1[1][1] == pair2[0][1]):
                count += 1
                
    return count


coords = [
    [0,0],
    [0,1],
    [0,2],
    [0,3],
    [1,0],
    [1,1],
    [1,2],
    [1,3],
]

coords = [
    [0,0],
    [0,1],
    [1,0],
    [1,1],
    [1,2],
    [2,1],
    [2,2],
    [2,3],
    [3,2],
    [3,3],
]

coords = [
    [1,1],
    [-1,1],
    [1,-5],
    [-1,-5],

]

# coords = [
#     [0,0],
#     [0,2],
#     [2,0],
#     [2,2],

#     [1,1],
#     [1,3],
#     [3,1],
#     [3,3],
# ]

coords = [
    [0,0],
    [0,1],
    [1,1],
    [1,0],
]
print(rectangleMania(coords))