def minTime(machines, goal):
    machines = sorted(machines)

    low_rate = machines[0]
    lowerBound = (goal // (len(machines) / low_rate))

    high_rate = machines[-1]
    upperBound = (goal // (len(machines) / high_rate)) + 1

    while lowerBound < upperBound:
        mid = (upperBound+lowerBound)//2
        items = itemsForDays(machines, mid)

        print(lowerBound,'-' ,upperBound, ',',mid, items)


        if items < goal:
            lowerBound = mid + 1
        else:
            upperBound = mid


    return int(lowerBound)

def itemsForDays(machines, days):
    items = 0
    for i in machines:
        items += (days//i)
    return items

machines = [2,3,2]
goal = 10
print(minTime(machines, goal))
# print(itemsForDays(machines, 8))