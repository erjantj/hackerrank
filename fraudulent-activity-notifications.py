def activityNotifications(arr, d, n):
    notifications = 0
    index_arr = [0]*200
    sortedd = [0]*d

    for i in range(d):
        index_arr[arr[i]] += 1

    median = 0
    prev = 0
    for i in range(d,n):
        itemsCount = 0
        prevCount = 0
        for j in range(200):
            prevCount = itemsCount
            itemsCount += index_arr[j]
            if d%2 == 0 and itemsCount > d//2:
                if prevCount != d//2:
                    median = j
                else:
                    median = (j+prev)/2
                break

            if d%2 == 1 and itemsCount > d//2:
                median = j
                break

            if index_arr[j] > 0:
                prev = j

        if median*2 <= arr[i]:
            notifications+=1

        index_arr[arr[i]] += 1
        index_arr[arr[i-d]] -= 1


    return notifications

with open('input.txt') as f:
    content = f.readlines()
    n, d = [int(x) for x in content[0].split()]
    arr = [int(x) for x in content[1].split()]
    
    print(activityNotifications(arr, d, n))
