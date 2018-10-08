def get_overlap(range1, range2):
    if range1[0] <= range2[1] and range2[0] <= range1[1]:
        return min(range1[1], range2[1])-max(range1[0], range2[0])
    return 0

def meeting_planner(slotsA, slotsB, dur):
    if not slotsA or not slotsB:
        return []

    if dur == 0:
        return []


    indexA = 0
    indexB = 0

    while indexA < len(slotsA) and indexB < len(slotsB):
        if slotsA[indexA][0]+dur > slotsA[indexA][1]:
            indexA += 1
            continue
        if slotsB[indexB][0]+dur > slotsB[indexB][1]:
            indexB += 1
            continue

        overlap = get_overlap(slotsA[indexA],slotsB[indexB])
        if overlap >= dur:
            maxSlotStart = max(slotsA[indexA][0], slotsB[indexB][0])
            return [maxSlotStart,maxSlotStart+dur]
        else:
            if slotsA[indexA][0] <= slotsB[indexB][0]:
                indexA += 1
            else:
                indexB += 1
    return []

# slotsA = [[0, 15], [60, 70]]
# slotsB = [[10, 50], [60, 120], [140, 210]]
# dur = 8

slotsA = [[0, 15], [60, 70]]
slotsB = [[10, 50], [60, 120], [140, 210]]
dur = 5


# slotsA = [[10, 50], [60, 120], [140, 210]]
# slotsB = [[0, 15], [60, 70]]
# dur = 12

print(meeting_planner(slotsA, slotsB, dur))

