def howManyAgentsToAdd(noOfCurrentAgents, callsTimes):
    callsTimes.sort(key=lambda x: x[0])
    callsTimesLen = len(callsTimes)

    overlaps = 0
    maxEnd = callsTimes[0][1]

    for i in range(callsTimesLen-1):
        lineMin = callsTimes[i]
        lineMax = callsTimes[i+1]
        if (min(lineMax[0], lineMax[1]) - max(lineMin[0], lineMin[1])) <= 0:
            overlaps += 1

        maxEndTmp = max(lineMax[1], lineMin[1])
        if maxEndTmp < maxEnd:
            maxEnd = maxEndTmp
            overlaps += 1
    print(overlaps)
    if overlaps == 0:
        return 0 

    return overlaps - noOfCurrentAgents

x = 1
# arr = [[1481122000, 1481122040], [1481122030, 1481122035], [1481122000, 1481122020]]
# arr = [[1481122000,1481122020],[1481122000,1481122040],[1481122030,1481122035]]
arr = [[1,5],[2,3],[4,7],[6,8]]
print(howManyAgentsToAdd(x, arr))

