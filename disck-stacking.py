def isLower(disk_above, disk):
    return disk_above[0] < disk[0] and disk_above[1] < disk[1] and disk_above[2] < disk[2]

def diskStacking(disks):
    result = []
    disks.sort(key=lambda disk: disk[2])
    dp = [(d[2],-1) for d in disks]
    max_index = 0
    max_heght = disks[max_index][2]
    for i in range(1, len(disks)):
        disk = disks[i]
        disk_max_height = disk[2]
        disk_above_index = -1
        for j in range(i):
            disk_above = disks[j]
            if isLower(disk_above, disk):
                disk_above_max_height, _ = dp[j]
                tmp_height = disk_above_max_height+disk[2]
                if tmp_height > disk_max_height:
                    disk_max_height = tmp_height
                    disk_above_index = j
        if disk_max_height > max_heght:
            max_heght = disk_max_height
            max_index = i
        dp[i] = (disk_max_height, disk_above_index)

    while max_index >= 0:
        result.append(disks[max_index])
        max_index = dp[max_index][1]
    return list(reversed(result))


disks = [[2,1,2],[3,2,3],[4,4,5],[2,2,8],[2,3,4],[1,3,1]]
# disks = [[4,4,5],[2,2,8],[2,3,6],[1,1,1]]
# disks = [[4,4,5]]
print(diskStacking(disks))

