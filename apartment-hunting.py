import sys
def apartmentHunting(blocks, reqs):
    perks = []
    for block in blocks:
        block_perks = set()
        for perk, exists in block.items():
            if exists:
                block_perks.add(perk)
        perks.append(block_perks)
    
    paths = [[sys.maxsize for j in reqs] for i in blocks]
    for i in range(len(perks)):
        block_perks = perks[i]
        for j in range(len(reqs)):
            req = reqs[j]
            if req in block_perks:
                paths[i][j] = 0
            elif i > 0 and j>= 0 and paths[i-1][j] >= 0:
                paths[i][j] = paths[i-1][j] + 1

    for i in range(len(perks)-1, -1, -1):
        block_perks = perks[i]
        for j in range(len(reqs)):
            req = reqs[j]
            if req in block_perks:
                paths[i][j] = min(paths[i][j], 0)
            elif i < len(perks)-1 and j < len(reqs) and paths[i+1][j] >= 0:
                paths[i][j] = min(paths[i][j], paths[i+1][j] + 1)

    min_index = 0
    min_val = max(paths[0])
    for index in range(len(paths)):
        row_max = max(paths[index])
        if row_max < min_val:
            min_val = row_max
            min_index = index

    return min_index

blocks = [
    {
        "gym": False,
        "school": True,
        "store": False
    },
    {
        "gym": True,
        "school": False,
        "store": False
    },
    {
        "gym": True,
        "school": True,
        "store": False
    },
    {
        "gym": False,
        "school": True,
        "store": False
    },
    {
        "gym": False,
        "school": True,
        "store": False
    }
]

reqs = ["store", "school", "gym"]
print(apartmentHunting(blocks, reqs))   