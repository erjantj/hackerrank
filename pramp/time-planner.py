def meeting_planner(slotsA, slotsB, dur):
    if not slotsA or not slotsB:
        return []

    if dur == 0:
        return []

    lower = []
    for slotA in slotsA:
        if slotA[0]+dur > slotA[1]:
            continue
        for slotB in slotsB:
            if slotB[0]+dur > slotB[1]:
                continue
            if slotA[0] >= slotB[0] and slotA[0]+dur <= slotB[1]:
                return [slotA[0],slotA[0]+dur]
            if slotB[0] >= slotA[0] and slotB[0]+dur <= slotA[1]:
                return [slotB[0],slotB[0]+dur]

    return []



# slotsA = [[0, 15], [60, 70]]
# slotsB = [[10, 50], [60, 120], [140, 210]]
# dur = 8

# slotsA = [[0, 15], [60, 70]]
# slotsB = [[10, 50], [50, 120], [140, 210]]
# dur = 8


slotsA = [[10, 50], [60, 120], [140, 210]]
slotsB = [[0, 15], [60, 70]]
dur = 12

print(meeting_planner(slotsA, slotsB, dur))